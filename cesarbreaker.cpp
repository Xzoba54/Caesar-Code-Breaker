#include <iostream>
#include <fstream>
#include <filesystem>
#include <optional>

enum class ExecutionMode{
     Break,
     Train,
     Help
};

struct ProgramConfig{
     ExecutionMode mode{ExecutionMode::Break};

     std::optional<std::string> inputText;
     std::optional<std::filesystem::path> inputFilePath;
     std::optional<std::filesystem::path> modelFilePath{"ngrams_probability.txt"};

     int ngramSize{3};
};

struct BaseError : std::runtime_error{
     explicit BaseError(std::string_view error) :
     std::runtime_error(std::string(error)) {}
};

struct MissingFlagValueError : public BaseError {
     MissingFlagValueError(std::string_view flag) :
     BaseError("Missing flag value " + std::string(flag)) {}
};

struct UnknownFlagError : public BaseError {
     UnknownFlagError(std::string_view flag) :
     BaseError("Unknown flag " + std::string(flag)) {}
};

class CLIParser{
public:
     static ProgramConfig parse(int argc, char* argv[]){
          ProgramConfig config;

          bool hasSourceFlag = false;
          int i = 1;
          while (i < argc){
               std::string_view arg = argv[i];
               if (arg == "-train"){
                    if (i + 1 >= argc){
                         throw MissingFlagValueError(arg);
                    }
                    config.mode = ExecutionMode::Train;
                    i += 1;
               }
               else if(arg == "-break"){
                    config.mode = ExecutionMode::Break;
               }
               else if (arg == "-n"){
                    if (i + 1 >= argc){
                         throw MissingFlagValueError(arg);
                    }
                    config.ngramSize = std::stoi(argv[i + 1]);
                    i += 1;
               }
               else if (arg == "-s"){
                    if(i + 1 >= argc){
                         throw MissingFlagValueError(arg);
                    }
                    config.inputFilePath = std::string(argv[i + 1]);
                    hasSourceFlag = true;
               }
               else if (arg.starts_with("-")){
                    throw UnknownFlagError(arg);
               }
               else{
                    if(!hasSourceFlag){
                         config.inputText = std::string(arg);
                    }
               }
               i += 1;
          }
          return config;
     }

     static void printHelp() {
          std::cout << "\t MODES\n";
          std::cout << "\t  -break     \t default mode\n";
          std::cout << "\t  -train\n\n";

          std::cout << "\t FLAGS\n";
          std::cout << "\t  -n <ngram> \t default 3\n";
          std::cout << "\t  -s <path>\t path to the input data with ciphertexts\n";
     }
};

class TextNormalizer{
public:
     TextNormalizer() = delete;

     static std::string normalize(std::string_view text){
          std::string result;

          std::size_t length = text.size();
          std::size_t i = 0;
          int bracket_depth = 0;

          result.reserve(length);

          while (i < length){
               unsigned char c = text[i];



               if(c == '('){
                    bracket_depth+=1;
                    i += 1;
                    continue;
               }
               else if (c == ')'){
                    bracket_depth-=1;
                    i += 1;
                    continue;
               }

               if (bracket_depth > 0){
                    i += 1;
                    continue;
               }

          }

          return result;
     }
};

int main(int argc, char* argv[]){
     try{
          CLIParser::parse(argc, argv);
     }
     catch(const UnknownFlagError& e){
          std::cerr << e.what() << "\n";

          CLIParser::printHelp();
          return EXIT_FAILURE;
     }
     catch(const BaseError& e){
          std::cerr << e.what() << "\n";
          return EXIT_FAILURE;
     }

     return 0;
}
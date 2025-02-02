class Logger:
    def log(self, message, tag):
        print(f"{tag} :  {message}")

def main():
    logger = Logger()
    logger.log("This is an information message.", "[INFO]")  
    logger.log("This is a warning message.", "[WARNING]")
    logger.log("This is an error message.", "[ERROR]")
main()
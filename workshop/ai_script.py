from core.modules import VisualNovelModule,ArtificialIntelligenceModule
from core.compiler import ai_compile

ai = ArtificialIntelligenceModule()

storyName = "demo" # This will be the name of the Json File

def script():

    return ai.aiDict


def main():ai_compile(storyName,script=script()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 

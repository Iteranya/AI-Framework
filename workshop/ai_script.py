from core.modules import VisualNovelModule,ArtificialIntelligenceModule
from core.compiler import ai_compile


from characters import Cupa,Andr # Import characters you've defined in characters.py
ai = ArtificialIntelligenceModule()
c = Cupa 
a = Andr
p = "Player" 
storyName = "demo" # This will be the name of the Json File

def story():

    return ai.aiDict


def main():ai_compile(storyName,script=story()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 

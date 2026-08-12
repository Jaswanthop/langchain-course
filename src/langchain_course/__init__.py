from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI # pyright: ignore[reportMissingImports]
from langchain_ollama import ChatOllama



load_dotenv()


def main() -> None:
    print("Hello from langchain!")
    information="""Walter Hartwell White, also known by his alias Heisenberg, is a fictional character and the protagonist of the American crime drama television series Breaking Bad. He is portrayed by Bryan Cranston.

Walter is a skilled chemist who co-founded a technology firm before he accepted a buy-out from his partners. While his partners became wealthy, Walter became a high school chemistry teacher in Albuquerque, New Mexico, barely making ends meet with his family: his wife Skyler (Anna Gunn) and their son Walter Jr. (RJ Mitte). At the start of the series, the day after his 50th birthday, he is diagnosed with Stage III lung cancer. After this discovery, Walter decides to manufacture and sell methamphetamine with his former student Jesse Pinkman (Aaron Paul), to ensure his family's financial security after his death. Due to his expertise, Walter's "blue meth" is purer than any other on the market, and he is pulled deeper into the illicit drug trade.

An antihero[a] turned villain protagonist as the series progresses, Walter becomes increasingly ruthless and unsympathetic, as the series' creator, Vince Gilligan, wanted him to turn from "Mr. Chips into Scarface". He adopts the alias "Heisenberg", which becomes recognizable as a kingpin figure in the Southwestern drug trade. Walter struggles with managing his family while hiding his involvement in the drug business from his brother-in-law, Hank Schrader (Dean Norris), an agent of the Drug Enforcement Administration. Although AMC officials initially hesitated to cast Cranston due to his previous comedic role in Malcolm in the Middle, Gilligan cast him based on his past performance in The X-Files episode "Drive", which Gilligan wrote. Cranston contributed greatly to the creation of his character, including Walter's backstory, personality, and physical appearance.
Both Walter and Cranston's performance have received critical acclaim, and Walter has frequently been mentioned as one of the greatest and most iconic television characters ever created. Cranston won four Primetime Emmy Awards for Outstanding Lead Actor in a Drama Series, three of them being consecutive. He is the first man to win a Critics' Choice, Golden Globe, Primetime Emmy, and Actor Award for his performance. Cranston reprised the role in a flashback for Breaking Bad's sequel film, El Camino: A Breaking Bad Movie, and again in the sixth and final season of the prequel series Better Call Saul, making him one of the few characters to appear in all three, alongside Jesse Pinkman, Mike Ehrmantraut (Jonathan Banks), Ed Galbraith (Robert Forster) and Austin Ramey (Todd Terry)."""
    summary_template = f"""given the following information about a character, please provide a summary of the character in 2-3 sentences. Information: {information}"""
    summary_prompt_template=PromptTemplate(input_variables=["information"], template=summary_template)
    #llm=ChatOpenAI(model="gpt-5", temperature=0)
    #composes of two components, the prompt template and the llm model
    model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=None,
    timeout=None,
    max_retries=2,
    #
)
   # model = ChatOllama(model="gemma3:4b",temperatue=0)
    chain=summary_prompt_template | model
    response=chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()

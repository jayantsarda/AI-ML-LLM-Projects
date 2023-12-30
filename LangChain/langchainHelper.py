from langchain.llms import OpenAI
from datasets import load_dataset
import sys
sys.path.insert(1, '/Users/jaysarda/Documents/AI-ML-LLM-Projects/AI-ML-LLM-Projects')
import Secrets
import os
from langchain.chains import SequentialChain

# creating prompt template

from langchain.prompts import PromptTemplate


os.environ['OPENAI_API_KEY'] = Secrets.OPENAI_API_KEY
llm = OpenAI(temperature=0.6)
#name = llm(prompt_template_name.format(cuisine = 'Mexican'))
#print(name)

# Create a chain
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain # one input -> one output
###name_chain  = LLMChain(llm=llm, prompt=prompt_template_name) #uncomment to run Simple Sequential chain
#print(name_chain.run('American'))

# Create SimpleSequential chain


##chain = SimpleSequentialChain(chains = [name_chain,food_item_chain]) #uncomment to run Simple Sequential chain

#print(chain.run('Indian'))

# Create Sequential chain : Multiple input and output

def generate_restaurent_name_and_menu_items(cuisine):

    prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template = 'Suggest a name for  {cuisine} restaurent')

    prompt_template_item = PromptTemplate(
    input_variables=['restaurant_name'],
    template = 'Suggest few bulleted Menu item for {restaurant_name} restaurent')

    food_item_chain  = LLMChain(llm=llm, prompt=prompt_template_item)
    name_chain_SequentialChain  = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    food_item_chain_SequentialChain  = LLMChain(llm=llm, prompt=prompt_template_item, output_key="menu_items")
    chain_SequentialChain = SequentialChain(
        chains = [name_chain_SequentialChain,food_item_chain_SequentialChain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name','menu_items']
        )
    response = chain_SequentialChain({'cuisine':cuisine})
    return response
# readme  - pip3 install langchain openai 

#if __name__ == "__main__":
    #print(generate_restaurent_name_and_menu_items("Italian"))
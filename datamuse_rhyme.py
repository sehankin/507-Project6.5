import requests
import json
import random

# Datamuse API: https://www.datamuse.com/api/

def find_rhyme_on_datamuse(word):
    datamuse_rhyme_url = "https://api.datamuse.com/words?rel_rhy=" + word
    datamuse_rhyme_reqget = requests.get(datamuse_rhyme_url).text  # JSON list
    datamuse_rhyme_result = json.loads(datamuse_rhyme_reqget)  # Python list
    rhyme_list = []
    for rhyme_dct in datamuse_rhyme_result:
        rhyme_list.append(rhyme_dct["word"])
    random_index = random.randrange(0, len(rhyme_list))
    chosen_rhyme = rhyme_list[random_index]
    return chosen_rhyme

#cat_rhyme = find_rhyme_on_datamuse("cat")
#print(cat_rhyme)

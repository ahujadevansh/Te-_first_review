import json 


with open('dataset/AMAZON_FASHION.json') as json_file: 
    data = [json.loads(line) for line in json_file] 

with open('dataset/meta_AMAZON_FASHION.json') as meta_json_file:
    meta_data = dict()
    for line in meta_json_file:
        temp = json.loads(line)
        meta_data[temp['asin']] = temp

dataset = []

for i in range(len(data)):
    meta = meta_data[data[i]['asin']]
    if(data[i]['overall'] in (1,5)):
        data[i].update(meta)


# data_file = open('dataset.json', 'w')
extreme_positive = open('dataset/positive_reviews.json', 'w')
extreme_negative = open('dataset/negative_reviews.json', 'w')

i=0
j=0
for dat in data:
    temp = dict()
    try:
        temp['rating'] = dat['overall']
        temp['reviewText'] = dat['reviewText']
        temp['title'] = dat['title']
        temp['asin'] = dat['asin']
        if(temp['rating'] == 1 and i<10000):
            extreme_negative.write(json.dumps(temp))
            extreme_negative.write('\n')
            i = i+1
        elif (j<10000):
            extreme_positive.write(json.dumps(temp))
            extreme_positive.write('\n')
            j = j+1
        # data_file.write(json.dumps(temp))
        # data_file.write('\n')
    except KeyError:
        pass

extreme_positive.close()
extreme_negative.close()

       
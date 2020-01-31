import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('AMAZON_FASHION.json') as json_file: 
    data = [json.loads(line) for line in json_file] 

with open('meta_AMAZON_FASHION.json') as meta_json_file:
    meta_data = [json.loads(line) for line in meta_json_file]

meta_dict = {}

for dat in meta_data:
    meta_dict[dat['asin']] = dat

# now we will open a file for writing 
negative_file = open('positive_reviews.csv', 'w')
positive_file = open('negative_reviews.csv', 'w')
# create the csv writer object 
positive_writer = csv.writer(positive_file) 
negative_writer = csv.writer(negative_file) 

header = ['overall', 'asin', 'reviewText', 'summary', 'title', 'description', 'brand', 'price']
positive_writer.writerow(header)
negative_writer.writerow(header)

for review in data:
    try:
        if(review['overall'] in (1,5)):
            dat = [review['overall'], review['asin'], review['reviewText'], review['summary']]
            meta_dat = meta_dict[review['asin']]
            dat.append(meta_dat['title'])
            dat.append(meta_dat['description'])
            dat.append(meta_dat['brand'])
            dat.append(meta_dat['price'])
            if(review['overall'] == 1):
                positive_writer.writerow(dat)
            else:
                negative_writer.writerow(dat)
    except KeyError:
        pass
    except UnicodeEncodeError:
        pass
  
positive_file.close()
negative_file.close() 

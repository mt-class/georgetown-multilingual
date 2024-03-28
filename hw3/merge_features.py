import sys
import pandas as pd

unique_args_string = ""

# This is the dumbest way to get the list of all languages, but it is late at night and I'm tired
langs = {}
for arg in sys.argv[1:]:
  #print(arg)
  with open(arg) as f:
    for line in f:
      line = line.rstrip('\n')
      lang, value = line.split(',')
      #print(lang)
      #print(value)
      if lang not in langs:
        langs[lang] = []
#print(langs)

# Now add features
for arg in sys.argv[1:]:
  with open(arg) as f:
    features = {}
    for line in f:
      line = line.rstrip('\n')
      lang, value = line.split(',')
      #print(lang)
      #print(value)
      features[lang] = value
    for lang in langs:
      if lang not in features:
        feature = -1
      else:
        feature = features[lang]
      values = langs[lang]
      values.append(feature)
      langs[lang] = values
  unique_args_string = unique_args_string + str(arg)
print(langs)

df = pd.DataFrame(langs).T
print(df)
#print(df.T)
print("writing to file:", unique_args_string)
df.to_csv(unique_args_string)

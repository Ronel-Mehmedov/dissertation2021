from html_similarity import style_similarity, structural_similarity, similarity

one = open("/home/x/allDataBackup/scamDeliverers/swiftlinelogistic.com/HTML/!").read()
second = open("/home/x/allDataBackup/legitDeliverers/aahvet.com/HTML/main").read()

print(type(one))
print(similarity(one, second))
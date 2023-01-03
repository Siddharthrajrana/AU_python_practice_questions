def find_and_replace(string):
    not_index = string.find('not')
    poor_index = string.find('poor')

    if (not_index < poor_index) and (poor_index < string.find('bad' , poor_index)):
        string = string[:not_index] + 'good ' + string[poor_index+4:]

    return string

print(find_and_replace('the food was not very good '))
        
        

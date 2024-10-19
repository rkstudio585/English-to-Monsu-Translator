# Further expanded dictionary for English to Monsu translation
english_to_monsu = {
    'hello': 'monsu_1',
    'world': 'monsu_2',
    'this': 'monsu_3',
    'is': 'monsu_4',
    'a': 'monsu_5',
    'test': 'monsu_6',
    'translator': 'monsu_7',
    'python': 'monsu_8',
    'code': 'monsu_9',
    'example': 'monsu_10',
    'language': 'monsu_11',
    'program': 'monsu_12',
    'good': 'monsu_13',
    'morning': 'monsu_14',
    'evening': 'monsu_15',
    'night': 'monsu_16',
    'how': 'monsu_17',
    'are': 'monsu_18',
    'you': 'monsu_19',
    'thank': 'monsu_20',
    'please': 'monsu_21',
    'welcome': 'monsu_22',
    'name': 'monsu_23',
    'yes': 'monsu_24',
    'no': 'monsu_25',
    'friend': 'monsu_26',
    'family': 'monsu_27',
    'food': 'monsu_28',
    'water': 'monsu_29',
    'house': 'monsu_30',
    'car': 'monsu_31',
    'city': 'monsu_32',
    'love': 'monsu_33',
    'happy': 'monsu_34',
    'sad': 'monsu_35',
    'beautiful': 'monsu_36',
    'fast': 'monsu_37',
    'slow': 'monsu_38',
    'strong': 'monsu_39',
    'weak': 'monsu_40',
    'run': 'monsu_41',
    'walk': 'monsu_42',
    'talk': 'monsu_43',
    'read': 'monsu_44',
    'write': 'monsu_45',
    'eat': 'monsu_46',
    'drink': 'monsu_47',
    'sleep': 'monsu_48',
    'work': 'monsu_49',
    'play': 'monsu_50',
    'school': 'monsu_51',
    'teacher': 'monsu_52',
    'student': 'monsu_53',
    'book': 'monsu_54',
    'pen': 'monsu_55',
    'computer': 'monsu_56',
    'internet': 'monsu_57',
    'music': 'monsu_58',
    'song': 'monsu_59',
    'dance': 'monsu_60',
    'phone': 'monsu_61',
    'call': 'monsu_62',
    'help': 'monsu_63',
    'day': 'monsu_64',
    'night': 'monsu_65',
    'happy': 'monsu_66',
    'birthday': 'monsu_67',
    'year': 'monsu_68',
    'month': 'monsu_69',
    'week': 'monsu_70',
    'today': 'monsu_71',
    'tomorrow': 'monsu_72',
    'yesterday': 'monsu_73',
    'big': 'monsu_74',
    'small': 'monsu_75',
    'hot': 'monsu_76',
    'cold': 'monsu_77',
    'sun': 'monsu_78',
    'moon': 'monsu_79',
    'star': 'monsu_80',
    'tree': 'monsu_81',
    'flower': 'monsu_82',
    'animal': 'monsu_83',
    'bird': 'monsu_84',
    'fish': 'monsu_85',
    'cat': 'monsu_86',
    'dog': 'monsu_87',
    'train': 'monsu_88',
    'bus': 'monsu_89',
    'airplane': 'monsu_90',
}

# Function to translate English to Monsu
def english_to_monsu_translator(text):
    # Split the input text into words
    words = text.lower().split()
    
    # Translate each word
    translated_words = []
    for word in words:
        # Check if the word exists in the dictionary, if not keep it as is
        translated_word = english_to_monsu.get(word, word)
        translated_words.append(translated_word)
    
    # Join the translated words into a sentence
    return ' '.join(translated_words)

# Example usage
english_text = input("Enter Text You Want to translate: ")
monsu_translation = english_to_monsu_translator(english_text)
print("Original:", english_text)
print("Translated to Monsu:", monsu_translation)

import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import scrapper as scrap

model = load_model('model.h5')
#model = load_model("model")
list = ['afghan_hound',
 'airedale',
 'appenzeller',
 'basenji',
 'beagle',
 'bernese_mountain_dog',
 'blenheim_spaniel',
 'bluetick',
 'border_terrier',
 'boston_bull',
 'boxer',
 'briard',
 'bull_mastiff',
 'cardigan',
 'chihuahua',
 'clumber',
 'collie',
 'dandie_dinmont',
 'dingo',
 'english_foxhound',
 'english_springer',
 'eskimo_dog',
 'french_bulldog',
 'german_short-haired_pointer',
 'golden_retriever',
 'great_dane',
 'greater_swiss_mountain_dog',
 'ibizan_hound',
 'irish_terrier',
 'irish_wolfhound',
 'japanese_spaniel',
 'kelpie',
 'komondor',
 'labrador_retriever',
 'leonberg',
 'malamute',
 'maltese_dog',
 'miniature_pinscher',
 'miniature_schnauzer',
 'norfolk_terrier',
 'norwich_terrier',
 'otterhound',
 'pekinese',
 'pomeranian',
 'redbone',
 'rottweiler',
 'saluki',
 'schipperke',
 'scottish_deerhound',
 'shetland_sheepdog',
 'siberian_husky',
 'soft-coated_wheaten_terrier',
 'standard_poodle',
 'sussex_spaniel',
 'tibetan_terrier',
 'toy_terrier',
 'walker_hound',
 'welsh_springer_spaniel',
 'whippet',
 'yorkshire_terrier']

d = {'boston_bull' : 'boston-terrier',
  'dingo' : 'carolina-dog',
 'pekinese' : 'pekingese',
 'bluetick' : 'bluetick-coonhound',
 'walker_hound' : 'treeing-walker-coonhound',
 'maltese_dog' : 'maltese',
 'redbone' : 'redbone-coonhound',
 'appenzeller' : 'appenzeller-sennenhund',
 'kelpie' : 'australian-kelpie',
 'malamute' : 'alaskan-malamute',
 'airedale' : 'airedale-terrier',
 'leonberg' : 'leonberger',
 'bull_mastiff' : 'bullmastiff',
 'cardigan' : 'cardigan-welsh-corgi',
 'clumber' : 'clumber-spaniel',
 'eskimo_dog' : 'american-eskimo-dog',
 'toy_terrier' : 'toy-fox-terrier',
 'dandie_dinmont' : 'dandie-dinmont-terrier',
 'standard_poodle' : 'poodle-standard',
 'japanese_spaniel' : 'japanese-chin',
 'blenheim_spaniel' : 'cavalier-king-charles-spaniel',
 'german_short_haired_pointer' : 'german-shorthaired-pointer',
 'english_springer' : 'english-springer-spaniel'}

def preprocess_image(uploaded_file):
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))
    img_arr = np.array(img)
    img_arr = np.expand_dims(img_arr, axis=0)/224
    return img_arr

def classifier(img_arr):
    pred_d = model.predict(img_arr)
    pred_labels = np.argmax(pred_d)
    return pred_labels


def app():
    st.title('Dog Breed Recognition System')
    st.image('banner.png')
    # Add file uploader to allow user to select an image
    st.markdown('>>**_Breed Indentifier_**')
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    # If an image file was uploaded
    if uploaded_file is not None:
        st.image(uploaded_file)
        img_arr = preprocess_image(uploaded_file)
        label = classifier(img_arr)

        button_clicked = st.button("Click Here To Identify!")
        if button_clicked:
            st.write(f"The Bread of the Dog is {list[label].replace('_', ' ').replace('-', ' ').title()}")
            try:
                for i, j in d.items():
                    if (list[label] == i):
                        list[label] = j
                        break
            except:
                pass
            for i in range(len(list)):
                list[i] = list[i].replace(" ", "-").replace("_", "-")
            st.markdown('>>**_Description of Your Buddy_**')
            st.write(scrap.info(list[label]))
            st.write('**_Vital Stats:-_**')
            scrap.stats(list[label])
            st.write(">>**_Bring Happiness To Your Home By Adopting_**")
            st.write("[Click Here To Adopt a {}](https://marketplace.akc.org/puppies/{})".format(list[label].replace('-', ' ').replace('_', ' ').title(), list[label]))

        gender_list = ['Select', 'Male', 'Female']
        st.write(">>**_Get A Name For Your New Buddy_**")
        gender = st.selectbox("Select a Gender from the dropdown", gender_list)
        if gender!='Select':
            name_lst = scrap.name(gender)
            for i in range(0, 10):
                st.write(f"Name Option {i+1} -> {name_lst[i]}")
if __name__ == '__main__':
    app()

#Email Subject Line Creator
# based on <https://clickhole.com/tips-for-crafting-the-perfect-email-subject-line-1825120753/>

# sea life facts are mostly from:
#   <seawifs.gsfc.nasa.gov/OCEAN_PLANET/HTML/education_marine_life_factsheet.html>
#   <http://www.uwphotographyguide.com/10-underwater-creature-facts>

from __future__ import print_function

import random
import os

def main():
    sea_life_facts=[]
    beautiful_words=[]
    # locate resources regardless of directory from which this is called
    script_dir=os.path.dirname(os.path.abspath(__file__))
    resources=os.path.join(script_dir,"resources")

    # load resources from files
    with open(os.path.join(resources,"sea_life_facts.txt"),"r") as f:
        contents=f.read()
        sea_life_facts=[item for item in contents.split("\n") if (item!="")]
    with open(os.path.join(resources,"beautiful_words.txt"),"r") as f:
        contents=f.read()
        beautiful_words=[item for item in contents.split("\n") if (item!="")]

    print("EMAIL SUBJECT LINE CREATOR EXTRAORDINAIRE")

    #Start off with GOOD EMAIL
    subj = "GOOD EMAIL "

    # add upsidedown question mark
    subj = subj+u'\u00BF '

    # add sea life fact if boss
    ans = input("Is the recipient of this email your boss? (y/n) ")
    r = 0 # r actuall = random number within size of slf
    if ans[0].lower() == 'y':
        r=random.randint(0,len(sea_life_facts)-1)
        subj = subj + sea_life_facts[r] + " "
        
    # add aaaaa
    subj = subj + "aaaaa "

    #add a beautiful word
    r=random.randint(0,len(beautiful_words)-1)
    subj = subj + beautiful_words[r] + " "
        
    # don't take a stance on Jeremy Piven either way
    ans = input("Would you like to take a stance on Jeremy Piven? ")
    if ans[0].lower() == 'y':
        print("Sorry, this is a poor choice for an email subject line.")
    else:
        print("Good choice.")
        
    #add Regarding The Position
    subj = subj + "Regarding The Position "

    #add a beautiful word
    r=random.randint(0,len(beautiful_words)-1)
    subj = subj + beautiful_words[r] + " "

    # I HAVE YOUR DAUGHTER / YOU HAVE A DAUGHTER if urgent
    ans = input("Is the email urgent? ")
    if ans[0].lower() == 'y':
        daughter = input("Does the recipient have a daughter? ")
        if daughter.lower() == 'y':
            subj = subj + "I HAVE YOUR DAUGHTER "
        else:
            subj = subj + "YOU HAVE A DAUGHTER "
        
    # add I love you if indicated
    ans = input("Do you love the recipient of this email? ")
    if ans[0].lower() == 'y':
        #add a beautiful word
        r=random.randint(0,len(beautiful_words)-1)
        subj = subj + beautiful_words[r] + " "
        subj = subj + "I love you "

    # add email recipient's address at the end
    email = input("What is the email address of the recipient? ")
    subj = subj + email

    print("\nYour subject line:")
    print(subj)


if __name__ == "__main__":
    main()
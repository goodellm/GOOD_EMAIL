#Email Subject Line Creator
# based on <www.clickhole.com/article/tips-crafting-perfect-email-subject-line-1729>
# sea life facts are mostly from:
#   <seawifs.gsfc.nasa.gov/OCEAN_PLANET/HTML/education_marine_life_factsheet.html>
#   <http://www.uwphotographyguide.com/10-underwater-creature-facts>
import random

seaLifeFacts = ['The blue whale is the largest animal known to have ever lived. ', 'Hydrothermal vents in the sea floor allow ecosystems to exist without energy from the sun. ', 'The oarfish is the longest bony fish in the world. ', 'Green turtles can migrate more than 1,400 miles to lay their eggs. ', 'A group of herring is called a seige. ', 'A group of jellyfish is called a smack. ', 'Bluefin tuna are among the largest and fastest of marine fish. ', 'Penguins "fly" underwater at speeds of up to 25mph. ', 'Horseshoe crabs have existed in essentially the same form for the past 135 million years. ','Many bony fish have more than just one set of nostrils. ','Not all Hermit Crabs use discarded seashells as their portable shelters. ','Sharks are covered with tiny little teeth called dermal denticles. ','Damselfish are farmers growing little algae gardens. ','Moray Eels open and close their mouths, not as an aggressive behavior but as part of their respiration process.','At night Parrotfish enclose themselves in a bubble of their own mucus to avoid being smelled by predators. ','Many species of fish are hermaphrodites. ','Barnacles are actually crustaceans related to crabs and lobsters. ']
beautifulWords = ['mellifluous ', 'nefarious ', 'epoch ', 'ethereal ', 'iridescent ', 'syzygy ', 'effervescence ', 'turbulence ', 'assemblage ', 'becoming ', 'dalliance ', 'elixir ', 'halcyon ', 'labyrinthine ','eudaimonia ','ephemeral ','coruscating ','quantum ','equilibrium ','email ','pheasant ','downpour ','schist ','geological ', 'enzyme ','xylem ','flourish ', 'swashbuckling']

print "EMAIL SUBJECT LINE CREATOR EXTRAORDINAIRE"

#Start off with GOOD EMAIL
subj = "GOOD EMAIL "

# add upsidedown question mark
subj = subj+u'\u00BF '

# add sea life fact if boss
ans = raw_input("Is the recipient of this email your boss? (y/n) ")
r = 0 # r actuall = random number within size of slf
if ans[0].lower() == 'y':
    r=random.randint(0,len(seaLifeFacts)-1)
    subj = subj + seaLifeFacts[r]
    
# add aaaaa
subj = subj + "aaaaa "

#add a beautiful word
r=random.randint(0,len(beautifulWords)-1)
subj = subj + beautifulWords[r]
    
# don't take a stance on Jeremy Piven either way
ans = raw_input("Would you like to take a stance on Jeremy Piven? ")
if ans[0].lower() == 'y':
    print "Sorry, this is a poor choice for an email subject line."
else:
    print "Good choice."
    
#add Regarding The Position
subj = subj + "Regarding The Position "

#add a beautiful word
r=random.randint(0,len(beautifulWords)-1)
subj = subj + beautifulWords[r]

# I HAVE YOUR DAUGHTER / YOU HAVE A DAUGHTER if urgent
ans = raw_input("Is the email urgent? ")
if ans[0].lower() == 'y':
    daughter = raw_input("Does the recipient have a daughter? ")
    if daughter.lower() == 'y':
        subj = subj + "I HAVE YOUR DAUGHTER "
    else:
        subj = subj + "YOU HAVE A DAUGHTER "
       
# add I Love You if indicated
ans = raw_input("Do you love the recipient of this email? ")
if ans[0].lower() == 'y':
    #add a beautiful word
    r=random.randint(0,len(beautifulWords)-1)
    subj = subj + beautifulWords[r]
    subj = subj + "I love you "

# add email recipient's address at the end
email = raw_input("What is the email address of the recipient? ")
subj = subj + email

print "\nYour subject line:"
print subj

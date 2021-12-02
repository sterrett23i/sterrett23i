print("This is not a replacement for a doctor. If your symptoms are serious, please see a doctor and protect yourself and others.")
understand = input("Do you understand? Please type yes or no.")
if understand == "no":
  print("Please accept these terms.")
  exit(1)
print("Program continuing, one moment please.") 
while True:
  print("The following next steps will prompt a major symptom in common illnesses, please type yes if it fits within your symptoms. The system will then prompt you with a secondary list of symptoms. Please type yes if the majority of symptoms fit. Reminder, this is NOT a diagnosis.")
  understand = input("Do you understand? Please type yes or no.")
  if understand == "yes":
    break
print("Major symptom: New loss of taste or smell")
symptom = input("Is this a major symptom of yours? Please type yes or no.")
if symptom == "yes":
  print("Other symptoms include; Fever and chills, cough, shortness of breath, fatigue, muscle or body aches, Headache, Sore Throat, Congestion or Runny Nose, Nausea or Vomiting, Diarrhea")
  symptom2 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom2 == "yes":
    print("Potential Infection Detected: Sars-Cov2 or Covid-19, Potential testing options include: PCR or Polymerase Chain Reaction is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. An antigen test may be suitable for rapid test results, these tests are accurate in positive results but negative results must be corroborated by a negative molecular test (PCR testing usually)")
    exit(1)
print("Major symptom: Raised pink or red bumps (papules), small fluid-filled blisters (vesicles), crusts and scabs")
symptom5 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom5 == "yes":
  print("Other symptoms include: Fever, loss of appetite, headache, tiredness and a general feeling of being unwell (malaise)")
  symptom6 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom6 == "yes":
    print("Potential Infection Detected: Chickenpox (Varicella), Potential testing options include: PCR or Polymerase Chain Reaction is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. These tests often use bacteria from the lesions on the skin.")
    exit(1)
print("Major symptom: Tiny white spots with bluish-white centers on a red background found inside the mouth on the inner lining of the cheek, also called Koplik's spots")
symptom7 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom7 == "yes":
  print("Other symptoms include: Fever, dry cough, runny nose, sore throat, inflamed eyes (conjunctivitis), a skin rash made up of large, flat blotches that often flow into one another")
  symptom8 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom8 == "yes":
    print("Potential Infection Detected: Mumps, Measles, and Rubella (MMR), Potential testing options include: Antibody test may be used to either diagnose MMR or decide whether or not you are immune to the MMR virus already. Antibody tests often use blood samples to run. A molecular test such as RT-PCR may often be used to diagnose an ongoing infection of Measles, Mumps, or Rubella.")
    exit(1)
print("Major symptom: Stiff neck and/or photophobia (eyes being more sensitive to light)")
symptom9 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom9 == "yes":
  print("Other symptoms include: Fever, headache, sleepiness or trouble waking up from sleep, nausea, irritability, vomiting, lack of appetite, lethargy")
  symptom10 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom10 == "yes":
    print("Potential Infection Detected: Viral Meningitis, Potential testing options include: PCR or Polymerase Chain Reaction is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. PCR tests to diagnose meningitis usually use spinal fluid from a spinal tap. A Gram's Stain test may also be used which is a form of serology.")
    exit(1)
print("Major symptom: Sharp or stabbing chest pain that gets worse when you breathe deeply or cough and/or A cough which may produce greenish, yellow or even bloody mucus")
symptom11 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom11 == "yes":
  print("Other symptoms include: Fever, sweating and shaking chills, shortness of breath, rapid, shallow breathing, loss of appetite, low energy, and fatigue, nausea and vomiting, especially in small children, confusion, especially in older people")
  symptom12 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom12 == "yes":
    print("Potential Infection Detected: Viral Pneumonia, Potential testing options include: Antigen test is suitable for rapid results, however serology (blood) tests are common. Viral cultures are also common when testing for Viral Pneumonia. More recently, Viral Pneumonia can be tested by using PCR or Polymerase Chain Reaction which is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. ")
    exit(1)
print("Major symptom: Swollen lymph nodes in the neck and armpits and/or swollen liver or spleen or both")
symptom13 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom13 == "yes":
  print("Other symptoms include: Extreme fatigue, fever, sore throat, head and body aches, rash")
  symptom14 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom14 == "yes":
    print("Potential Infection Detected: Infectious Mononucleosis, Potential testing options include: Antibody testing using blood samples. These tests often look at specific antibodies only found when someone is infected with mononucleosis. Other serology (blood) test may be used to look at white blood cell and platelet counts.")
    exit(1)
print("Major symptom: Red and swollen tonsils, sometimes with white patches or streaks of pus and/or tiny, red spots (Petechiae) on the roof of the mouth")
symptom15 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom15 == "yes":
  print("Other symptoms include: Sore throat that can start very quickly, pain when swallowing, fever, Red and swollen tonsils, swollen lymph nodes in the front of the neck")
  symptom16 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom16 == "yes":
    print("Potential Infection Detected: Strep Throat (Streptococcal Pharyngitis), Potential testing options include: PCR or Polymerase Chain Reaction is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. These PCR tests often use pharyngeal testing. An antigen test may be suitable for rapid test results, these tests are accurate in positive results but negative results must be corroborated by a negative molecular test (PCR testing usually) ")
    exit(1)
print("Major symptom: Aching Muscles")
symptom3 = input("Is this a major symptom of yours? Please type yes or no.")
if symptom3 == "yes":
  print("Other symptoms include: Fever, chills and sweats, headache, dry, persistent cough, shortness of breath, tiredness and weakness, Runny or stuffy nose, sore throat, eye pain, vomiting and diarrhea (is more common in children than adults)")
  symptom4 = input("Do the majority of these symptoms fit? Please type yes or no.")
  if symptom4 == "yes":
    print("Potential Infection Detected: Influenza, Potential testing options include: PCR or Polymerase Chain Reaction is a molecular test that is highly accurate in detecting ongoing infections however it takes about 1-3 days before results come back at most testing locations. An antigen test may be suitable for rapid test results, these tests are accurate in positive results but negative results must be corroborated by a negative molecular test (PCR testing usually)")
    exit(1)
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import scrolledtext, font, messagebox
from textblob import TextBlob
import datetime
import json
import re
import random

# --- Language Content Data ---
# (The LANG_DATA dictionary remains exactly the same as in your original code)
LANG_DATA = {
    'en': {
        'title': "Digital Literacy Chatbot",
        'lang_select_prompt': "Please select a language for the chatbot:",
        'lang_desc': "English",
        'welcome': "Hello! I am your Digital Literacy Chatbot. I can help you learn about online safety and skills. Type 'info' for more, 'quiz' to test your knowledge, 'agri' for agriculture tips, 'health' for health information, 'skills' for education details, 'sanitation' for cleanliness tips, 'emergency' for helpline numbers, 'digital_india' for a new initiative, 'make_in_india' for another initiative, 'joke' for a laugh, or 'image' to generate one! You can also ask about the 'time', 'date', or 'weather'. Type 'creator' to know who made me.",
        'info_intro': "🌐 What is Digital Literacy?",
        'info_content': "Digital literacy is the ability to use digital devices like computers, mobile phones, and the internet correctly. It helps us in online services, banking, education, and communication.\n\nExamples:\n - Using online banking\n - Sending emails\n - Creating strong passwords\n - Following cybersecurity rules",
        'security_tips': "🔒 Online Security Tips",
        'security_content': "Cybersecurity is key for online safety.\n1. **OTP Warning**: Never share your One-Time Password (OTP) with anyone, not even bank employees. An OTP is for your use only.\n2. **Phishing**: Be cautious of suspicious emails or messages asking for personal information.\n3. **Strong Passwords**: Use a mix of letters, numbers, and special characters.\n4. **Public Wi-Fi**: Avoid sensitive transactions (like banking) on public Wi-Fi networks.",
        'quiz_intro': "📝 Let's do a quick quiz:\n",
        'q1': "1️⃣ Question: What should a strong password include?",
        'q1_options': "a) Only names\nb) A mix of letters, numbers, and special characters\nc) Date of birth",
        'q1_ans': 'b',
        'q2': "2️⃣ Question: What should you do with a link sent by an unknown person?",
        'q2_options': "a) Click on it immediately\nb) Ignore it\nc) Share it with everyone",
        'q2_ans': 'b',
        'q3': "3️⃣ Question: Should you share your OTP with a bank representative?",
        'q3_options': "a) Yes\nb) No, never\nc) Only if they call you from a bank number",
        'q3_ans': 'b',
        'q4': "4️⃣ Question: What is phishing?",
        'q4_options': "a) Fishing in a pond\nb) Trying to steal personal information using fake emails\nc) A type of online game",
        'q4_ans': 'b',
        'q5': "5️⃣ Question: Is it safe to do online banking on public Wi-Fi?",
        'q5_options': "a) Yes\nb) No, it's risky\nc) Only if the Wi-Fi is free",
        'q5_ans': 'b',
        'correct': "Correct! ✅",
        'incorrect': "Incorrect. ❌ The correct answer is: ",
        'your_score': "🎉 Your final score: ",
        'quiz_end_excellent': "Great job! You're a digital literacy expert.",
        'quiz_end_good': "You're on the right track! A little more practice will make you an expert.",
        'quiz_end_average': "Keep learning! Practice makes perfect.",
        'nlp_positive': "Your feedback is much appreciated! Thanks for the positive words. 😊",
        'nlp_negative': "I'm sorry to hear that. How can I improve to better assist you? 🤔",
        'nlp_neutral': "Okay, I understand. If you have any questions, feel free to ask. 🧐",
        'unknown_command': "I'm sorry, I don't understand that command. Please try 'info', 'quiz', 'security', 'agri', 'health', 'skills', 'sanitation', 'emergency', 'digital_india', 'make_in_india', 'joke', 'image', 'creator', 'time', 'date', or 'weather'.",
        'otp_warning': "🚫 SECURITY ALERT: It looks like you mentioned an OTP. Remember, never share your One-Time Password with anyone, even if they claim to be from a bank or any other service. Stay safe online!",
        'time': "The current time is: ",
        'date': "Today's date is: ",
        'weather': "Current weather in Lucknow: {weather_desc}",
        'image_prompt': "Please describe the image you want me to generate.",
        'image_generating': "🎨 Generating your image: '{prompt}'. This may take a moment...",
        'image_link': "🖼️ Your image is ready! View it here: ",
        'joke_intro': "😂 Here's a joke for you:",
        'jokes': [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why was the computer cold? Because it left its Windows open!",
            "I'm on a seafood diet. I see food, and I eat it.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        'agri_intro': "🌾 Agriculture and Government Schemes",
        'agri_content': "Agriculture is the science and practice of cultivating plants and livestock. Here are some key Government schemes that help farmers:\n\n - **Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)**: An income support scheme for farmers.\n Link: https://pmkisan.gov.in/\n\n - **Pradhan Mantri Fasal Bima Yojana (PMFBY)**: A crop insurance scheme to protect farmers from losses.\n Link: https://pmfby.gov.in/\n\n - **Kisan Credit Card (KCC)**: A scheme to provide timely credit to farmers.\n Link: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **Pradhan Mantri Krishi Sinchai Yojana (PMKSY)**: Aims to provide assured irrigation to every farm in the country.\n Link: https://pmksy.gov.in/\n\n - **GOBARdhan Scheme**: A 'Waste to Wealth' initiative for rural areas to convert solid waste and cattle dung into useful resources like biogas and organic manure.\n Link: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 Health Consultation and Schemes",
        'health_content': "Here's how you can get health consultations and information about government health schemes:\n\n - **eSanjeevani**: A national telemedicine service by the Government of India that offers free online doctor consultations.\n Link: https://esanjeevani.mohfw.gov.in/\n\n - **Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)**: The world's largest health assurance scheme providing a health cover of ₹5 lakh per family per year for poor and vulnerable families.\n Link: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 Sanitation Awareness",
        'sanitation_content': "Sanitation awareness is crucial for community health. The Government of India has launched a massive campaign to promote hygiene and cleanliness.\n\n - **Swachh Bharat Mission (SBM)**: A nationwide campaign to eliminate open defecation and improve solid waste management. It provides financial assistance for building toilets in both rural and urban areas.\n Link: https://swachhbharatmission.gov.in/\n\n - **Role of National Health Mission (NHM)**: NHM focuses on improving health outcomes, which are directly linked to sanitation and hygiene. It works to create awareness about healthy sanitation practices to prevent diseases.",
        'skills_intro': "🎓 Skills and Education",
        'skills_content': "Skill development and education are essential for individual growth and national progress. Here are key government initiatives:\n\n - **Pradhan Mantri Kaushal Vikas Yojana (PMKVY)**: The flagship scheme to enable a large number of Indian youth to take up industry-relevant skill training to secure a better livelihood.\n Link: https://pmkvyofficial.org/\n\n - **National Education Policy (NEP) 2020**: A comprehensive policy aimed at transforming India's education system. It integrates vocational and skill-based learning into the mainstream curriculum from an early age.\n Link: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 Digital India",
        'digital_india_content': "The Digital India program aims to transform India into a digitally empowered society and a knowledge economy. Key initiatives include:\n\n - **DigiLocker**: Provides a digital space for citizens to store and access their official documents securely.\n - **BharatNet**: Aims to provide high-speed internet connectivity to all Gram Panchayats.",
        'make_in_india_intro': "🇮🇳 Make in India",
        'make_in_india_content': "The 'Make in India' initiative encourages companies to manufacture their products in India. The goal is to boost economic growth, create jobs, and attract foreign investment.",
        'emergency_intro': "🚨 Emergency and Helpline Support",
        'emergency_content': "In case of an emergency, you can use these helpline numbers:\n\n - **All-in-one Emergency Number**: **112** (Police, Fire, Ambulance)\n - **Police**: **100**\n - **Fire**: **101**\n - **Ambulance**: **108**\n - **Disaster Management**: **1078**\n - **Women's Helpline**: **1091**\n - **Kisan Call Centre (for farmers)**: **1800-180-1551**",
        'creator': "This chatbot was created by Anup Yadav (student of BBD University, resident of Siwan, Bihar) with programming by Ankit Singh.",
        'log_message': "User question logged."
    },
    'hi': {
        'title': "डिजिटल साक्षरता चैटबॉट",
        'lang_select_prompt': "चैटबॉट के लिए एक भाषा चुनें:",
        'lang_desc': "हिंदी (Hindi)",
        'welcome': "नमस्ते! मैं आपका डिजिटल साक्षरता चैटबॉट हूँ। मैं आपको ऑनलाइन सुरक्षा और कौशल के बारे में जानने में मदद कर सकता हूँ। जानकारी के लिए 'info', अपने ज्ञान का परीक्षण करने के लिए 'quiz', कृषि की जानकारी के लिए 'agri', स्वास्थ्य की जानकारी के लिए 'health', शिक्षा के विवरण के लिए 'skills', स्वच्छता के लिए 'sanitation', आपातकालीन नंबरों के लिए 'emergency', 'digital_india' और 'make_in_india' जैसी नई योजनाओं के लिए भी पूछ सकते हैं, 'joke' के लिए चुटकुला या 'image' के लिए एक चित्र भी बना सकते हैं! आप 'समय', 'आज की तारीख', या 'मौसम' भी बता सकते हैं। मुझे किसने बनाया है ये जानने के लिए 'creator' टाइप करें।",
        'info_intro': "🌐 डिजिटल साक्षरता क्या है?",
        'info_content': "डिजिटल साक्षरता का अर्थ है कंप्यूटर, मोबाइल और इंटरनेट जैसे डिजिटल उपकरणों का सही उपयोग करना। यह हमें ऑनलाइन सेवाओं, बैंकिंग, शिक्षा और संचार के क्षेत्र में मदद करता है।\n\nउदाहरण:\n - ऑनलाइन बैंकिंग का उपयोग\n - ईमेल भेजना\n - सुरक्षित पासवर्ड बनाना\n - साइबर सुरक्षा के नियमों का पालन करना",
        'security_tips': "🔒 ऑनलाइन सुरक्षा टिप्स",
        'security_content': "ऑनलाइन सुरक्षा के लिए साइबर सुरक्षा बहुत महत्वपूर्ण है।\n1. **ओटीपी चेतावनी**: अपना वन-टाइम पासवर्ड (ओटीपी) कभी भी किसी के साथ साझा न करें, यहां तक ​​कि बैंक कर्मचारियों के साथ भी नहीं। ओटीपी केवल आपके उपयोग के लिए है।\n2. **फिशिंग**: व्यक्तिगत जानकारी मांगने वाले संदिग्ध ईमेल या संदेशों से सावधान रहें।\n3. **मजबूत पासवर्ड**: अक्षर, अंक और विशेष चिन्ह का मिश्रण उपयोग करें।\n4. **सार्वजनिक वाई-फाई**: सार्वजनिक वाई-फाई नेटवर्क पर संवेदनशील लेनदेन (जैसे बैंकिंग) से बचें।",
        'quiz_intro': "📝 चलिए एक छोटा सा क्विज़ करते हैं:\n",
        'q1': "1️⃣ सवाल: मजबूत पासवर्ड में क्या होना चाहिए?",
        'q1_options': "a) केवल नाम\nb) अक्षर, अंक और विशेष चिन्ह का मिश्रण\nc) जन्मतिथि",
        'q1_ans': 'b',
        'q2': "2️⃣ सवाल: अनजान व्यक्ति द्वारा भेजे गए लिंक पर क्या करना चाहिए?",
        'q2_options': "a) तुरंत क्लिक करें\nb) नजरअंदाज करें\nc) उसे सबको भेज दें",
        'q2_ans': 'b',
        'q3': "3️⃣ सवाल: क्या आपको अपना ओटीपी बैंक प्रतिनिधि के साथ साझा करना चाहिए?",
        'q3_options': "a) हाँ\nb) नहीं, कभी नहीं\nc) केवल तभी जब वे आपको बैंक नंबर से कॉल करें",
        'q3_ans': 'b',
        'q4': "4️⃣ सवाल: फिशिंग क्या है?",
        'q4_options': "a) तालाब में मछली पकड़ना\nb) फर्जी ईमेल का उपयोग करके व्यक्तिगत जानकारी चुराने की कोशिश\nc) एक प्रकार का ऑनलाइन खेल",
        'q4_ans': 'b',
        'q5': "5️⃣ सवाल: क्या सार्वजनिक वाई-फाई पर ऑनलाइन बैंकिंग करना सुरक्षित है?",
        'q5_options': "a) हाँ\nb) नहीं, यह जोखिम भरा है\nc) केवल तभी जब वाई-फाई मुफ़्त हो",
        'q5_ans': 'b',
        'correct': "सही! ✅",
        'incorrect': "गलत। ❌ सही उत्तर है: ",
        'your_score': "🎉 आपका अंतिम स्कोर: ",
        'quiz_end_excellent': "बहुत बढ़िया! आप डिजिटल साक्षरता के विशेषज्ञ हैं।",
        'quiz_end_good': "आप सही रास्ते पर हैं! थोड़ा और अभ्यास आपको विशेषज्ञ बना देगा।",
        'quiz_end_average': "सीखते रहें! अभ्यास से ही सब कुछ संभव है।",
        'nlp_positive': "आपकी प्रतिक्रिया बहुत सराहनिय है! सकारात्मक शब्दों के लिए धन्यवाद। 😊",
        'nlp_negative': "मुझे यह सुनकर खेद है। मैं आपकी बेहतर सहायता कैसे कर सकता हूँ? 🤔",
        'nlp_neutral': "ठीक है, मैं समझता हूँ। यदि आपके कोई प्रश्न हैं, तो पूछने में संकोच न करें। 🧐",
        'unknown_command': "मुझे खेद है, मुझे वह कमांड समझ में नहीं आया। कृपया 'info', 'quiz', 'security', 'agri', 'health', 'skills', 'sanitation', 'emergency', 'digital_india', 'make_in_india', 'joke', 'image', 'creator', 'time', 'date', या 'weather' का प्रयास करें।",
        'otp_warning': "🚫 सुरक्षा चेतावनी: ऐसा लगता है कि आपने ओटीपी का उल्लेख किया है। याद रखें, अपना वन-टाइम पासवर्ड किसी के साथ साझा न करें, भले ही वे बैंक या किसी अन्य सेवा से होने का दावा करें। ऑनलाइन सुरक्षित रहें!",
        'time': "वर्तमान समय है: ",
        'date': "आज की तारीख है: ",
        'weather': "लखनऊ में वर्तमान मौसम: {weather_desc}",
        'image_prompt': "कृपया उस चित्र का वर्णन करें जिसे आप मुझसे बनवाना चाहते हैं।",
        'image_generating': "🎨 आपका चित्र बनाया जा रहा है: '{prompt}'। इसमें कुछ समय लग सकता है...",
        'image_link': "🖼️ आपका चित्र तैयार है! इसे यहां देखें: ",
        'joke_intro': "😂 आपके लिए एक चुटकुला है:",
        'jokes': [
            "पुलिस वाले ने चोर से कहा, 'तुम्हारे पास जूते क्यों नहीं हैं?' चोर बोला, 'मैं भागते समय जूते क्यों पहनूँ?'",
            "टीचर: 'तुम रोज स्कूल क्यों नहीं आते?' विद्यार्थी: 'सर, मैं रोज आता हूँ, पर मेरा दिमाग घर पर रह जाता है!'",
            "गोलू: 'यार, मैं अपनी बीवी के लिए क्या खरीदूँ?' मोलू: 'तेरे पास कौन सा फोन है?' गोलू: 'iPhone 15 Pro Max' मोलू: 'तो फिर अपनी बीवी के लिए iPhone 16 Pro Max खरीद ले!'",
            "एक आदमी ने अपनी बीवी से कहा, 'मैं घर छोड़ कर जा रहा हूँ!' बीवी बोली, 'तो ठीक है, मैं भी घर छोड़ कर जा रही हूँ!' आदमी: 'तो मैं कहाँ जाऊँ?'"
        ],
        'agri_intro': "🌾 कृषि और सरकारी योजनाएँ",
        'agri_content': "कृषि पौधों और पशुओं की खेती का विज्ञान और अभ्यास है। यहां कुछ महत्वपूर्ण सरकारी योजनाएं हैं जो किसानों की मदद करती हैं:\n\n - **प्रधान मंत्री किसान सम्मान निधि (PM-KISAN)**: किसानों के लिए एक आय सहायता योजना।\n लिंक: https://pmkisan.gov.in/\n\n - **प्रधान मंत्री फसल बीमा योजना (PMFBY)**: किसानों को नुकसान से बचाने के लिए एक फसल बीमा योजना।\n लिंक: https://pmfby.gov.in/\n\n - **किसान क्रेडिट कार्ड (KCC)**: किसानों को समय पर ऋण प्रदान करने की एक योजना।\n लिंक: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **प्रधान मंत्री कृषि सिंचाई योजना (PMKSY)**: देश के हर खेत को सुनिश्चित सिंचाई प्रदान करने का लक्ष्य रखती है।\n लिंक: https://pmksy.gov.in/\n\n - **गोबरधन (GOBARdhan) योजना**: ग्रामीण क्षेत्रों के लिए 'कचरे से धन' की पहल, जिसमें ठोस कचरे और गोबर को बायोगैस और जैविक खाद जैसे उपयोगी संसाधनों में परिवर्तित किया जाता है।\n लिंक: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 स्वास्थ्य परामर्श और योजनाएँ",
        'health_content': "आप स्वास्थ्य परामर्श कैसे प्राप्त कर सकते हैं और सरकारी स्वास्थ्य योजनाओं के बारे में जानकारी यहाँ दी गई है:\n\n - **eSanjeevani**: भारत सरकार की एक राष्ट्रीय टेलीमेडिसिन सेवा जो मुफ्त ऑनलाइन डॉक्टर परामर्श प्रदान करती है।\n लिंक: https://esanjeevani.mohfw.gov.in/\n\n - **आयुष्मान भारत - प्रधान मंत्री जन आरोग्य योजना (PM-JAY)**: दुनिया की सबसे बड़ी स्वास्थ्य आश्वासन योजना जो गरीब और कमजोर परिवारों के लिए प्रति वर्ष प्रति परिवार ₹5 लाख का स्वास्थ्य कवर प्रदान करती है।\n लिंक: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 स्वच्छता जागरूकता",
        'sanitation_content': "समुदाय के स्वास्थ्य के लिए स्वच्छता जागरूकता महत्वपूर्ण है। भारत सरकार ने स्वच्छता और सफाई को बढ़ावा देने के लिए एक बड़ा अभियान शुरू किया है।\n\n - **स्वच्छ भारत मिशन (SBM)**: खुले में शौच को खत्म करने और ठोस कचरा प्रबंधन में सुधार के लिए एक राष्ट्रव्यापी अभियान। यह ग्रामीण और शहरी दोनों क्षेत्रों में शौचालय बनाने के लिए वित्तीय सहायता प्रदान करता है।\n लिंक: https://swachhbharatmission.gov.in/\n\n - **राष्ट्रीय स्वास्थ्य मिशन (NHM) की भूमिका**: NHM का ध्यान स्वास्थ्य परिणामों को बेहतर बनाने पर है, जो सीधे स्वच्छता और सफाई से जुड़े हैं। यह बीमारियों को रोकने के लिए स्वस्थ स्वच्छता प्रथाओं के बारे में जागरूकता पैदा करने का काम करता है।",
        'skills_intro': "🎓 कौशल और शिक्षा",
        'skills_content': "व्यक्तिगत विकास और राष्ट्र की प्रगति के लिए कौशल विकास और शिक्षा आवश्यक हैं। यहाँ कुछ प्रमुख सरकारी पहल हैं:\n\n - **प्रधान मंत्री कौशल विकास योजना (PMKVY)**: भारतीय युवाओं की बड़ी संख्या को उद्योग-प्रासंगिक कौशल प्रशिक्षण लेने में सक्षम बनाने की प्रमुख योजना ताकि वे बेहतर आजीविका सुरक्षित कर सकें।\n लिंक: https://pmkvyofficial.org/\n\n - **राष्ट्रीय शिक्षा नीति (NEP) 2020**: भारत की शिक्षा प्रणाली को बदलने के उद्देश्य से एक व्यापक नीति। यह कम उम्र से ही व्यावसायिक और कौशल-आधारित शिक्षा को मुख्यधारा के पाठ्यक्रम में एकीकृत करती है।\n लिंक: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 डिजिटल इंडिया",
        'digital_india_content': "डिजिटल इंडिया कार्यक्रम का उद्देश्य भारत को एक डिजिटल रूप से सशक्त समाज और ज्ञान अर्थव्यवस्था में बदलना है। मुख्य पहलों में शामिल हैं:\n\n - **डिजी लॉकर (DigiLocker)**: नागरिकों को अपने आधिकारिक दस्तावेजों को सुरक्षित रूप से संग्रहीत करने और उन तक पहुँचने के लिए एक डिजिटल स्थान प्रदान करता है।\n - **भारतनेट (BharatNet)**: सभी ग्राम पंचायतों को हाई-स्पीड इंटरनेट कनेक्टिविटी प्रदान करने का लक्ष्य रखता है।",
        'make_in_india_intro': "🇮🇳 मेक इन इंडिया",
        'make_in_india_content': "'मेक इन इंडिया' पहल कंपनियों को भारत में अपने उत्पादों का निर्माण करने के लिए प्रोत्साहित करती है। इसका लक्ष्य आर्थिक विकास को बढ़ावा देना, रोजगार पैदा करना और विदेशी निवेश को आकर्षित करना है।",
        'emergency_intro': "🚨 आपातकालीन और हेल्पलाइन सहायता",
        'emergency_content': "आपात स्थिति में, आप इन हेल्पलाइन नंबरों का उपयोग कर सकते हैं:\n\n - **ऑल-इन-वन आपातकालीन नंबर**: **112** (पुलिस, अग्निशमन, एम्बुलेंस)\n - **पुलिस**: **100**\n - **अग्निशमन**: **101**\n - **एम्बुलेंस**: **108**\n - **आपदा प्रबंधन**: **1078**\n - **महिला हेल्पलाइन**: **1091**\n - **किसान कॉल सेंटर (किसानों के लिए)**: **1800-180-1551**",
        'creator': "इस चैटबॉट को अनूप यादव (बीबीडी विश्वविद्यालय के छात्र, निवासी सीवान, बिहार) ने बनाया है और प्रोग्रामिंग अंकित सिंह ने की है।",
        'log_message': "उपयोगकर्ता का प्रश्न लॉग किया गया।"
    },
    'hing': {
        'title': "डिजिटल लिटरेसी चैटबॉट (Hinglish)",
        'lang_select_prompt': "Chatbot ke liye ek language choose karo:",
        'lang_desc': "Hinglish (Hindi + English)",
        'welcome': "Hello! Main aapka Digital Literacy Chatbot hoon. Main aapko online safety aur skills sikhane mein help kar sakta hoon. 'info' type karke aur jaano, 'quiz' se apna knowledge test karo, 'agri' se agriculture tips, 'health' se health information, 'skills' se education details, 'sanitation' se cleanliness tips, 'emergency' se helpline numbers, 'digital_india' aur 'make_in_india' jaise initiatives ke baare mein bhi pooch sakte hain, 'joke' se ek chukala suno ya 'image' se ek image generate karo! Aap 'time', 'date', ya 'weather' bhi pooch sakte ho. 'creator' type karke jaano ki mujhe kisne banaya hai.",
        'info_intro': "🌐 Digital Literacy kya hai?",
        'info_content': "Digital literacy ka matlab hai computer, mobile, aur internet jaise digital devices ko sahi tarike se use karna. Isse hum online services, banking, education aur communication mein help milti hai.\n\nExamples:\n - Online banking use karna\n - Emails send karna\n - Strong passwords banana\n - Cybersecurity rules follow karna",
        'security_tips': "🔒 Online Security Tips",
        'security_content': "Cybersecurity online safety ke liye bahut important hai.\n1. **OTP Warning**: Apna One-Time Password (OTP) kabhi bhi kisi ke saath share mat karo, bank employees ke saath bhi nahi. OTP sirf aapke use ke liye hai.\n2. **Phishing**: Suspicious emails ya messages se savdhan raho jo personal information maange.\n3. **Strong Passwords**: Letters, numbers, aur special characters ka mix use karo.\n4. **Public Wi-Fi**: Public Wi-Fi networks par sensitive transactions (jaise banking) avoid karo.",
        'quiz_intro': "📝 Chalo ek quick quiz karte hain:\n",
        'q1': "1️⃣ Question: Strong password mein kya hona chahiye?",
        'q1_options': "a) Sirf names\nb) Letters, numbers, aur special characters ka mix\nc) Date of birth",
        'q1_ans': 'b',
        'q2': "2️⃣ Question: Ek unknown person ke bheje hue link ka kya karna chahiye?",
        'q2_options': "a) Uspe turant click karo\nb) Usko ignore karo\nc) Usko sabke saath share karo",
        'q2_ans': 'b',
        'q3': "3️⃣ Question: Kya aapko apna OTP bank representative ke saath share karna chahiye?",
        'q3_options': "a) Yes\nb) No, bilkul nahi\nc) Only agar wo bank number se call kare",
        'q3_ans': 'b',
        'q4': "4️⃣ Question: Phishing kya hai?",
        'q4_options': "a) Paani mein fish pakadna\nb) Fake emails se personal information chori karne ki koshish\nc) Ek tarah ka online game",
        'q4_ans': 'b',
        'q5': "5️⃣ Question: Kya public Wi-Fi par online banking karna safe hai?",
        'q5_options': "a) Yes\nb) No, bilkul risky hai\nc) Sirf agar Wi-Fi free ho to",
        'q5_ans': 'b',
        'correct': "Correct! ✅",
        'incorrect': "Incorrect. ❌ Sahi jawab hai: ",
        'your_score': "🎉 Aapka final score: ",
        'quiz_end_excellent': "Great job! Aap ek digital literacy expert ho.",
        'quiz_end_good': "Aap sahi track par ho! Thoda aur practice aapko expert bana dega.",
        'quiz_end_average': "Seekhte raho! Practice makes perfect.",
        'nlp_positive': "Aapka feedback bahut accha laga! Positive words ke liye thanks. 😊",
        'nlp_negative': "I'm sorry to hear that. Main kaise aur better help kar sakta hoon? 🤔",
        'nlp_neutral': "Okay, main samajh gaya. Agar koi aur sawal ho to pooch sakte ho. 🧐",
        'unknown_command': "I'm sorry, main yeh command nahi samjha. Please try 'info', 'quiz', 'security', 'agri', 'health', 'skills', 'sanitation', 'emergency', 'digital_india', 'make_in_india', 'joke', 'image', 'creator', 'time', 'date', ya 'weather'.",
        'otp_warning': "🚫 SECURITY ALERT: Aisa lagta hai ki aapne OTP mention kiya hai. Yaad rakho, apna One-Time Password kisi ke saath share mat karo, bhale hi wo bank ya kisi aur service se hone ka daava kare. Online safe raho!",
        'time': "Current time hai: ",
        'date': "Aaj ka date hai: ",
        'weather': "Lucknow mein current weather: {weather_desc}",
        'image_prompt': "Please describe karo ki aap kaun si image generate karwana chahte ho.",
        'image_generating': "🎨 Aapki image generate ho rahi hai: '{prompt}'. Isme thoda time lag sakta hai...",
        'image_link': "🖼️ Aapki image ready hai! Yahan dekho: ",
        'joke_intro': "😂 Yeh lo ek joke:",
        'jokes': [
            "Pappu: 'Mummy, main kitna badmaash hoon?' Mummy: 'Pagal hai, tu to sher hai!' Pappu: 'To school mein ma'am mujhe chuha kyu kehti hai?'",
            "Teacher: 'Tumhara homework kahan hai?' Student: 'Sir, wo to kal hi ho gaya tha.' Teacher: 'To aaj kyu nahi hai?' Student: 'Sir, main roz-roz thodi na karta hoon!'",
            "Ek machhar ne doosre se kaha, 'Yaar, bahut garmi hai!' Doosra bola, 'To khet mein chalo, wahan AC hai.'",
            "Ek aadmi ne apni biwi se kaha, 'Main ghar chhod kar ja raha hoon!' Biwi boli, 'To theek hai, main bhi ghar chhod kar ja rahi hoon!' Aadmi: 'To main kahan jaaun?'"
        ],
        'agri_intro': "🌾 Agriculture aur Government Schemes",
        'agri_content': "Agriculture plants aur livestock ko cultivate karne ka science aur practice hai. Farmers ki help ke liye kuch important Government schemes hain:\n\n - **Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)**: Farmers ke liye ek income support scheme hai.\n Link: https://pmkisan.gov.in/\n\n - **Pradhan Mantri Fasal Bima Yojana (PMFBY)**: Farmers ko loss se bachane ke liye ek crop insurance scheme hai.\n Link: https://pmfby.gov.in/\n\n - **Kisan Credit Card (KCC)**: Farmers ko time par credit dene ki scheme.\n Link: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **Pradhan Mantri Krishi Sinchai Yojana (PMKSY)**: Iska aim hai country ke har farm ko assured irrigation provide karna.\n Link: https://pmksy.gov.in/\n\n - **GOBARdhan Scheme**: Rural areas ke liye ek 'Waste to Wealth' initiative, jisse solid waste aur cattle dung ko biogas aur organic manure jaise useful resources mein convert kiya jaata hai.\n Link: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 Health Consultation aur Schemes",
        'health_content': "Aap health consultations aur government health schemes ke baare mein yahan se information le sakte hain:\n\n - **eSanjeevani**: Government of India ki ek national telemedicine service hai jo free online doctor consultations deti hai.\n Link: https://esanjeevani.mohfw.gov.in/\n\n - **Ayushman Bharat - Pradhan Mantri Jan Arogya Yojana (PM-JAY)**: Duniya ki sabse badi health assurance scheme jo gareeb aur vulnerable families ko saal bhar ₹5 lakh tak ka health cover deti hai.\n Link: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 Sanitation Awareness",
        'sanitation_content': "Community health ke liye sanitation awareness bahut important hai. Government of India ne cleanliness aur hygiene ko promote karne ke liye ek bada campaign launch kiya hai.\n\n - **Swachh Bharat Mission (SBM)**: Open defecation ko eliminate karne aur solid waste management ko improve karne ke liye ek nationwide campaign. Ye rural aur urban dono areas mein toilets banane ke liye financial assistance deta hai.\n Link: https://swachhbharatmission.gov.in/\n\n - **National Health Mission (NHM) ka Role**: NHM health outcomes ko improve karne par focus karta hai, jo directly sanitation aur hygiene se linked hain. Ye diseases ko prevent karne ke liye healthy sanitation practices ke baare mein awareness create karta hai.",
        'skills_intro': "🎓 Skills aur Education",
        'skills_content': "Individual growth aur national progress ke liye skill development aur education bahut zaruri hain. Yahan kuch main government initiatives hain:\n\n - **Pradhan Mantri Kaushal Vikas Yojana (PMKVY)**: Indian youth ki ek badi population ko industry-relevant skill training dene ki flagship scheme taaki unki livelihood better ho sake.\n Link: https://pmkvyofficial.org/\n\n - **National Education Policy (NEP) 2020**: India ke education system ko transform karne ke liye ek comprehensive policy. Ye vocational aur skill-based learning ko early age se hi mainstream curriculum mein integrate karti hai.\n Link: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 Digital India",
        'digital_india_content': "Digital India program ka aim hai India ko ek digitally empowered society aur knowledge economy mein badalna. Main initiatives hain:\n\n - **DigiLocker**: Citizens ko unke official documents ko secure tarike se store aur access karne ke liye ek digital space deta hai.\n - **BharatNet**: Sabhi Gram Panchayats ko high-speed internet connectivity provide karne ka aim hai.",
        'make_in_india_intro': "🇮🇳 Make in India",
        'make_in_india_content': "'Make in India' initiative companies ko India mein apne products manufacture karne ke liye encourage karta hai. Iska goal hai economic growth ko boost karna, jobs create karna, aur foreign investment attract karna.",
        'emergency_intro': "🚨 Emergency aur Helpline Support",
        'emergency_content': "Emergency ke case mein, aap in helpline numbers ka use kar sakte hain:\n\n - **All-in-one Emergency Number**: **112** (Police, Fire, Ambulance)\n - **Police**: **100**\n - **Fire**: **101**\n - **Ambulance**: **108**\n - **Disaster Management**: **1078**\n - **Women's Helpline**: **1091**\n - **Kisan Call Centre (farmers ke liye)**: **1800-180-1551**",
        'creator': "Is chatbot ko Anup Yadav (BBD University ke student, Siwan, Bihar ke niwasi) ne banaya hai, aur programming Ankit Singh ne ki hai.",
        'log_message': "User ka question log ho gaya."
    },
    'awa': {
        'title': "डिजिटल साक्षरता चैटबॉट (अवधी)",
        'lang_select_prompt': "चैटबॉट खातिर एक भाषा चुना:",
        'lang_desc': "अवधी (Awadhi)",
        'welcome': "जय सियाराम! हम तुहार डिजिटल साक्षरता चैटबॉट हईं। हम तोहार ऑनलाइन सुरक्षा अउर हुनर सीखे में मदद कइ सकित हईं। 'info' लिखि के अउर जान्या, 'quiz' से आपन ज्ञान परखा, 'agri' से खेती-बाड़ी का सलाह, 'health' से स्वास्थ्य का जानकारी, 'skills' से पढ़ाई-लिखाई का जानकारी, 'sanitation' से सफाई का जानकारी, 'emergency' से आपातकालीन नंबरों का जानकारी, 'digital_india' और 'make_in_india' जइसे नई पहल के बारे में भी पूछी सकित हउवा, 'joke' से हँसे खातिर चुटकुला या 'image' से चित्र भी बनाइ सकित हउवा! हम तोहे 'समय', 'तारीख', या 'मौसम' भी बताइ सकित हईं। हमका के बनाइल हय इ जाने खातिर 'creator' टाइप करा।",
        'info_intro': "🌐 डिजिटल साक्षरता का हय?",
        'info_content': "डिजिटल साक्षरता का मतलब कंप्यूटर, मोबाइल, अउर इंटरनेट जइसे डिजिटल औज़ारन का सही उपयोग करब हय। इ हमका ऑनलाइन सेवा, बैंक का काम, पढ़ाई अउर बात-चीत करे में मदद करइ हय।\n\nउदाहरण:\n - ऑनलाइन बैंकिंग का उपयोग\n - ईमेल भेजइ\n - मजबूत पासवर्ड बनउब\n - साइबर सुरक्षा का नियम मानइ",
        'security_tips': "🔒 ऑनलाइन सुरक्षा",
        'security_content': "ऑनलाइन सुरक्षित रहे खातिर साइबर सुरक्षा बहुत जरूरी हय।\n1. **ओटीपी चेतावनी**: आपन वन-टाइम पासवर्ड (ओटीपी) केहू से न बतावा, चाहे उ बैंक के कर्मचारी ही काहें न होए। ओटीपी खाली तोहार उपयोग खातिर हय।\n2. **फिशिंग**: अइसे संदिग्ध ईमेल या संदेशन से बचि के रहा जे तोहार निजी जानकारी माँगे।\n3. **मजबूत पासवर्ड**: अक्षर, अंक, अउर खास चिन्हन का मेल उपयोग करा।\n4. **पब्लिक वाई-फाई**: पब्लिक वाई-फाई नेटवर्क पर संवेदनशील काम (जइसे बैंकिंग) करे से बची।",
        'quiz_intro': "📝 चला, एक ठौ छोटका क्विज़ करा जा:\n",
        'q1': "1️⃣ सवाल: एक मजबूत पासवर्ड में का होए चाही?",
        'q1_options': "a) खाली नाम\nb) अक्षर, अंक, अउर खास चिन्हन का मेल\nc) जनम तिथि",
        'q1_ans': 'b',
        'q2': "2️⃣ सवाल: अनजान मनई के भेजल लिंक पर का करब चाही?",
        'q2_options': "a) झट से ओपर क्लिक करा\nb) ओका छोड़ि द्या\nc) सबरे के साथ शेयर करा",
        'q2_ans': 'b',
        'q3': "3️⃣ सवाल: का तोहे आपन ओटीपी बैंक के आदमी से बतावब चाही?",
        'q3_options': "a) हाँ\nb) नाहीं, कबहुँ नाहीं\nc) खाली तब जब उ बैंक के नंबर से फोन करे",
        'q3_ans': 'b',
        'q4': "4️⃣ सवाल: फिशिंग का हय?",
        'q4_options': "a) पोखरा में मछरी पकड़ब\nb) फर्जी ईमेल का उपयोग कइके निजी जानकारी चोरइ का प्रयास\nc) एक तरह का ऑनलाइन खेल",
        'q4_ans': 'b',
        'q5': "5️⃣ सवाल: का सार्वजनिक वाई-फाई पर ऑनलाइन बैंकिंग करब सुरक्षित हय?",
        'q5_options': "a) हाँ\nb) नाहीं, इ खतरा भरा हय\nc) खाली तब जब वाई-फाई मुफ्त होय",
        'q5_ans': 'b',
        'correct': "सही हय! ✅",
        'incorrect': "गलत हय। ❌ सही उत्तर हय: ",
        'your_score': "🎉 तोहार आखिरी स्कोर: ",
        'quiz_end_excellent': "बहूत बढ़िया! आप डिजिटल साक्षरता के गुरु हउवा।",
        'quiz_end_good': "आप सही रास्ता पर हउवा! थोड़ि अउर अभ्यास तोहे गुरु बनाइ देई।",
        'quiz_end_average': "सीखत रहा! अभ्यास से सब कुछ बन जाइ हय।",
        'nlp_positive': "तोहार प्रतिक्रिया बहुत बढ़िया लागत हय! सकारात्मक शब्दन खातिर धन्यवाद्। 😊",
        'nlp_negative': "हमका इ सुनि के खेद हय। हम तोहार अउर अच्छा मदद कइसे कइ सकित हईं? 🤔",
        'nlp_neutral': "ठीक हय, हम समझि गइलीं। अगर तोहार कउनो अउर सवाल होए, तो पूछी सकित हउवा। 🧐",
        'unknown_command': "हमका खेद हय, हम इ कमांड नाहीं समझि पाइल। कृपया 'info', 'quiz', 'security', 'agri', 'health', 'skills', 'sanitation', 'emergency', 'digital_india', 'make_in_india', 'joke', 'image', 'creator', 'time', 'date', या 'weather' का प्रयोग करा।",
        'otp_warning': "🚫 सुरक्षा चेतावनी: लागत हय कि तू ओटीपी का जिक्र कइले हउवा। याद रखा, आपन वन-टाइम पासवर्ड केहू से ना बतावा, चाहे उ बैंक या कउनो दूसर सेवा से होय का दावा करे। ऑनलाइन सुरक्षित रहा!",
        'time': "वर्तमान समय हय: ",
        'date': "आज के तारीख हय: ",
        'weather': "लखनऊ में वर्तमान मौसम: {weather_desc}",
        'image_prompt': "कृपया उ चित्र का वर्णन करा जे तोहे बनवावब हय।",
        'image_generating': "🎨 तोहार चित्र बनइ रहल हय: '{prompt}'। इमे कुछ समय लाग सकत हय...",
        'image_link': "🖼️ तोहार चित्र तैयार हय! इहाँ देखा: ",
        'joke_intro': "😂 तोहार खातिर एक चुटकुला हय:",
        'jokes': [
            "पुलिस वाले चोर से कहले, 'तोहार लगे जूता काहे नाहीं हय?' चोर कहले, 'हम भागते समय जूता काहे पहनीं?'",
            "गुरुजी: 'तू रोज स्कूल काहे नाहीं आवत?' लरिका: 'गुरुजी, हम रोज आवत हईं, लेकिन हमार दिमाग घरै छूट जात हय!'",
            "गोलू: 'यार, हम आपन मेहरारु खातिर का खरीदीं?' मोलू: 'तोहार लगे कवन मोबाइल हय?' गोलू: 'iPhone 15 Pro Max' मोलू: 'तो आपन मेहरारु खातिर iPhone 16 Pro Max लेइ ल्या!'",
            "एक मनई आपन मेहरारु से कहले, 'हम घर छोडि के जात हई!' मेहरारु कहलस, 'तो ठीक हय, हम भी घर छोडि के जात हई!' मनई: 'तो हम कहाँ जाई?'"
        ],
        'agri_intro': "🌾 कृषि अउर सरकारी योजनाएँ",
        'agri_content': "कृषि पौध अउर जानवरन के खेती का विज्ञान अउर काम हय। इहाँ कुछ महत्वपूर्ण सरकारी योजनाएँ हइन जे किसानन के मदद करत हइन:\n\n - **प्रधान मंत्री किसान सम्मान निधि (PM-KISAN)**: किसानन खातिर एक आय सहायता योजना।\n लिंक: https://pmkisan.gov.in/\n\n - **प्रधान मंत्री फसल बीमा योजना (PMFBY)**: किसानन के नुकसान से बचावे खातिर एक फसल बीमा योजना।\n लिंक: https://pmfby.gov.in/\n\n - **किसान क्रेडिट कार्ड (KCC)**: किसानन के समय पर ऋण देवे का एक योजना।\n लिंक: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **प्रधान मंत्री कृषि सिंचाई योजना (PMKSY)**: देस के हर खेत के सुनिश्चित सिंचाई देवे का लक्ष्य रखत हय।\n लिंक: https://pmksy.gov.in/\n\n - **गोबरधन (GOBARdhan) योजना**: ग्रामीण इलाकन खातिर 'कचरे से धन' का पहल, जेमे ठोस कचरा अउर गोबर का उपयोग करके बायोगैस अउर जैविक खाद जइसे उपयोगी संसाधन बनउल जाइ हय।\n लिंक: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 स्वास्थ्य परामर्श अउर योजनाएँ",
        'health_content': "आप स्वास्थ्य परामर्श कइसे प्राप्त कइ सकित हउवा अउर सरकारी स्वास्थ्य योजनान के बारे में जानकारी इहाँ दीन्ह गयल हय:\n\n - **eSanjeevani**: भारत सरकार के एक राष्ट्रीय टेलीमेडिसिन सेवा जे मुफ्त ऑनलाइन डॉक्टर परामर्श देत हय।\n लिंक: https://esanjeevani.mohfw.gov.in/\n\n - **आयुष्मान भारत - प्रधान मंत्री जन आरोग्य योजना (PM-JAY)**: दुनिया के सबसे बड़ स्वास्थ्य आश्वासन योजना जे गरीब अउर कमजोर परिवारन खातिर प्रति वर्ष प्रति परिवार ₹5 लाख का स्वास्थ्य कवर देत हय।\n लिंक: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 स्वच्छता जागरूकता",
        'sanitation_content': "समुदाय के स्वास्थ्य खातिर स्वच्छता जागरूकता जरूरी हय। भारत सरकार सफाई अउर स्वच्छता के बढ़ावा देवे खातिर एक बड़ अभियान चलाइले हय।\n\n - **स्वच्छ भारत मिशन (SBM)**: खुले में शौच का खतम करे अउर ठोस कचरा प्रबंधन के सुधारे खातिर एक देस-व्यापी अभियान। इ ग्रामीण अउर शहरी दुइनो इलाकन में शौचालय बनउवे खातिर आर्थिक मदद देत हय।\n लिंक: https://swachhbharatmission.gov.in/\n\n - **राष्ट्रीय स्वास्थ्य मिशन (NHM) के भूमिका**: NHM का ध्यान स्वास्थ्य का परिणाम सुधारे पर हय, जे सीधा स्वच्छता अउर सफाई से जुड़ल हय। इ बीमारी के रोके खातिर स्वस्थ स्वच्छता का आदत के बारे में जागरूकता पैदा करइ हय।",
        'skills_intro': "🎓 कौशल अउर शिक्षा",
        'skills_content': "व्यक्तिगत विकास अउर राष्ट्र के प्रगति खातिर कौशल विकास अउर शिक्षा जरूरी हय। इहाँ कुछ प्रमुख सरकारी पहल हइन:\n\n - **प्रधान मंत्री कौशल विकास योजना (PMKVY)**: भारतीय जवानन के एक बड़ संख्या के उद्योग से जुड़ल कौशल प्रशिक्षण देवे का मुख्य योजना ताकि उ एक अच्छा आजीविका सुरक्षित कइ सकइ।\n लिंक: https://pmkvyofficial.org/\n\n - **राष्ट्रीय शिक्षा नीति (NEP) 2020**: भारत के शिक्षा प्रणाली के बदले का मकसद से एक व्यापक नीति। इ कम उम्र से ही व्यावसायिक अउर कौशल-आधारित शिक्षा के मुख्य धारा का पाठ्यक्रम में जोड़इ हय।\n लिंक: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 डिजिटल इंडिया",
        'digital_india_content': "डिजिटल इंडिया कार्यक्रम का मकसद भारत के एक डिजिटल रूप से सशक्त समाज अउर ज्ञान अर्थव्यवस्था में बदलइ हय। मुख्य पहल में शामिल हइन:\n\n - **डिजी लॉकर (DigiLocker)**: नागरिकन के आपन आधिकारिक दस्तवेजन के सुरक्षित रूप से रखई अउर उन तक पहुँचइ खातिर एक डिजिटल जगह देत हय।\n - **भारतनेट (BharatNet)**: सबरे ग्राम पंचायतन के हाई-स्पीड इंटरनेट कनेक्टिविटी देवे का मकसद रखत हय।",
        'make_in_india_intro': "🇮🇳 मेक इन इंडिया",
        'make_in_india_content': "'मेक इन इंडिया' पहल कंपनियों के भारत में आपन उत्पाद बनावे खातिर प्रोत्साहित करइ हय। एकर मकसद आर्थिक विकास के बढ़ावा देब, रोजगार पैदा करब, अउर विदेशी निवेश के आकर्षित करब हय।",
        'emergency_intro': "🚨 आपातकालीन अउर हेल्पलाइन सहायता",
        'emergency_content': "आपात स्थिति में, आप इ हेल्पलाइन नंबर का उपयोग कइ सकित हउवा:\n\n - **ऑल-इन-वन आपातकालीन नंबर**: **112** (पुलिस, अग्निशमन, एम्बुलेंस)\n - **पुलिस**: **100**\n - **अग्निशमन**: **101**\n - **एम्बुलेंस**: **108**\n - **आपदा प्रबंधन**: **1078**\n - **महिला हेल्पलाइन**: **1091**\n - **किसान कॉल सेंटर (किसानन खातिर)**: **1800-180-1551**",
        'creator': "इ चैटबॉट के अनूप यादव (बीबीडी विश्वविद्यालय के छात्र, सीवान, बिहार के निवासी) बनउले हइन अउर प्रोग्रामिंग अंकित सिंह कइले हइन।",
        'log_message': "उपयोगकर्ता का सवाल लॉग होइ गयल।"
    },
    'guj': {
        'title': "ડિજિટલ સાક્ષરતા ચેટબોટ",
        'lang_select_prompt': "ચેટબોટ માટે એક ભાષા પસંદ કરો:",
        'lang_desc': "ગુજરાતી (Gujarati)",
        'welcome': "નમસ્કાર! હું તમારો ડિજિટલ સાક્ષરતા ચેટબોટ છું. હું તમને ઓનલાઈન સુરક્ષા અને કૌશલ્યો વિશે શીખવામાં મદદ કરી શકું છું. વધુ જાણકારી માટે 'info' લખો, તમારા જ્ઞાનને ચકાસવા માટે 'quiz', ખેતી વિશે જાણવા માટે 'agri', આરોગ્ય વિશે જાણવા માટે 'health', શિક્ષણ વિશેની માહિતી માટે 'skills', સ્વચ્છતા વિશે જાણવા માટે 'sanitation', કટોકટીના નંબરો માટે 'emergency', 'digital_india' અને 'make_in_india' જેવી નવી પહેલ વિશે પણ પૂછી શકો છો, 'joke' માટે જોક્સ અથવા 'image' માટે એક ચિત્ર પણ બનાવી શકો છો! હું તમને 'સમય', 'તારીખ', અથવા 'હવામાન' પણ જણાવી શકું છું. મને કોણે બનાવ્યો છે તે જાણવા માટે 'creator' લખો.",
        'info_intro': "🌐 ડિજિટલ સાક્ષરતા એટલે શું?",
        'info_content': "ડિજિટલ સાક્ષરતા એટલે કમ્પ્યુટર, મોબાઈલ અને ઈન્ટરનેટ જેવા ડિજિટલ ઉપકરણોનો યોગ્ય રીતે ઉપયોગ કરવાની ક્ષમતા. તે આપણને ઓનલાઈન સેવાઓ, બેંકિંગ, શિક્ષણ અને સંદેશાવ્યવહારમાં મદદ કરે છે.\n\nઉદાહરણો:\n - ઓનલાઈન બેંકિંગનો ઉપયોગ\n - ઈમેલ મોકલવા\n - મજબૂત પાસવર્ડ બનાવવા\n - સાયબર સુરક્ષાના નિયમોનું પાલન કરવું",
        'security_tips': "🔒 ઓનલાઈન સુરક્ષા ટિપ્સ",
        'security_content': "ઓનલાઈન સુરક્ષા માટે સાયબર સુરક્ષા ચાવીરૂપ છે.\n1. **OTP ચેતવણી**: તમારો વન-ટાઇમ પાસવર્ડ (OTP) ક્યારેય કોઈની સાથે શેર કરશો નહીં, બેંક કર્મચારીઓ સાથે પણ નહીં. OTP ફક્ત તમારા ઉપયોગ માટે છે.\n2. **ફિશિંગ**: શંકાસ્પદ ઇમેઇલ્સ અથવા સંદેશાઓથી સાવચેત રહો જે વ્યક્તિગત માહિતી માંગે છે.\n3. **મજબૂત પાસવર્ડ**: અક્ષરો, સંખ્યાઓ અને વિશેષ અક્ષરોનું મિશ્રણ વાપરો.\n4. **પબ્લિક વાઇ-ફાઇ**: પબ્લિક વાઇ-ફાઇ નેટવર્ક પર સંવેદનશીલ વ્યવહારો (જેમ કે બેંકિંગ) કરવાનું ટાળો.",
        'quiz_intro': "📝 ચાલો એક નાની ક્વિઝ કરીએ:\n",
        'q1': "1️⃣ પ્રશ્ન: મજબૂત પાસવર્ડમાં શું શામેલ હોવું જોઈએ?",
        'q1_options': "a) માત્ર નામો\nb) અક્ષરો, સંખ્યાઓ અને વિશેષ અક્ષરોનું મિશ્રણ\nc) જન્મતારીખ",
        'q1_ans': 'b',
        'q2': "2️⃣ પ્રશ્ન: કોઈ અજાણી વ્યક્તિ દ્વારા મોકલવામાં આવેલી લિંકનું શું કરવું જોઈએ?",
        'q2_options': "a) તેના પર તરત ક્લિક કરો\nb) તેને અવગણો\nc) તેને બધા સાથે શેર કરો",
        'q2_ans': 'b',
        'q3': "3️⃣ પ્રશ્ન: શું તમારે તમારો OTP બેંક પ્રતિનિધિ સાથે શેર કરવો જોઈએ?",
        'q3_options': "a) હા\nb) ના, ક્યારેય નહીં\nc) ફક્ત જો તેઓ તમને બેંક નંબરથી કોલ કરે તો",
        'q3_ans': 'b',
        'q4': "4️⃣ પ્રશ્ન: ફિશિંગ શું છે?",
        'q4_options': "a) તળાવમાં માછલી પકડવી\nb) નકલી ઇમેઇલ્સનો ઉપયોગ કરીને વ્યક્તિગત માહિતી ચોરી કરવાનો પ્રયાસ\nc) એક પ્રકારની ઓનલાઇન રમત",
        'q4_ans': 'b',
        'q5': "5️⃣ પ્રશ્ન: શું પબ્લિક વાઇ-ફાઇ પર ઓનલાઇન બેંકિંગ કરવું સુરક્ષિત છે?",
        'q5_options': "a) હા\nb) ના, તે જોખમી છે\nc) ફક્ત જો વાઇ-ફાઇ મફત હોય તો",
        'q5_ans': 'b',
        'correct': "સાચું! ✅",
        'incorrect': "ખોટું. ❌ સાચો જવાબ છે: ",
        'your_score': "🎉 તમારો અંતિમ સ્કોર: ",
        'quiz_end_excellent': "ખૂબ સરસ! તમે ડિજિટલ સાક્ષરતાના નિષ્ણાત છો.",
        'quiz_end_good': "તમે સાચા માર્ગ પર છો! થોડો વધુ અભ્યાસ તમને નિષ્ણાત બનાવશે.",
        'quiz_end_average': "શીખતા રહો! અભ્યાસથી બધું શક્ય બને છે.",
        'nlp_positive': "તમારા પ્રતિભાવની ખૂબ પ્રશંસા થાય છે! સકારાત્મક શબ્દો માટે આભાર. 😊",
        'nlp_negative': "આ સાંભળીને મને દુઃખ થયું. હું તમને વધુ સારી રીતે કેવી રીતે મદદ કરી શકું? 🤔",
        'nlp_neutral': "બરાબર, હું સમજું છું. જો તમને કોઈ પ્રશ્નો હોય, તો પૂછવા માટે મફત રહો. 🧐",
        'unknown_command': "માફ કરશો, હું તે આદેશ સમજી શકતો નથી. કૃપા કરીને 'info', 'quiz', 'security', 'agri', 'health', 'skills', 'sanitation', 'emergency', 'digital_india', 'make_in_india', 'joke', 'image', 'creator', 'time', 'date', અથવા 'weather' નો પ્રયાસ કરો.",
        'otp_warning': "🚫 સુરક્ષા ચેતવણી: એવું લાગે છે કે તમે OTP નો ઉલ્લેખ કર્યો છે. યાદ રાખો, તમારો વન-ટાઇમ પાસવર્ડ ક્યારેય કોઈની સાથે શેર કરશો નહીં, ભલે તેઓ બેંક અથવા અન્ય કોઈ સેવાના હોવાનો દાવો કરે. ઓનલાઇન સુરક્ષિત રહો!",
        'time': "વર્તમાન સમય છે: ",
        'date': "આજની તારીખ છે: ",
        'weather': "લખનઉમાં વર્તમાન હવામાન: {weather_desc}",
        'image_prompt': "કૃપા કરીને તમે જે ચિત્ર બનાવવા માંગો છો તેનું વર્ણન કરો.",
        'image_generating': "🎨 તમારું ચિત્ર જનરેટ થઈ રહ્યું છે: '{prompt}'। આમાં થોડો સમય લાગી શકે છે...",
        'image_link': "🖼️ તમારું ચિત્ર તૈયાર છે! તેને અહીં જુઓ: ",
        'joke_intro': "😂 અહીં તમારા માટે એક જોક છે:",
        'jokes': [
            "પોલીસવાળાએ ચોરને કહ્યું, 'તારી પાસે બુટ કેમ નથી?' ચોર બોલ્યો, 'હું ભાગતી વખતે બુટ કેમ પહેરું?'",
            "ટીચર: 'તમે રોજ શાળાએ કેમ આવતા નથી?' વિદ્યાર્થી: 'સર, હું રોજ આવું છું, પણ મારું મગજ ઘરે રહી જાય છે!'",
            "ગોલુ: 'યાર, હું મારી પત્ની માટે શું ખરીદું?' મોલુ: 'તારી પાસે કયો ફોન છે?' ગોલુ: 'iPhone 15 Pro Max' મોલુ: 'તો પછી તારી પત્ની માટે iPhone 16 Pro Max ખરીદી લે!'",
            "એક માણસે પોતાની પત્નીને કહ્યું, 'હું ઘર છોડીને જઈ રહ્યો છું!' પત્ની બોલી, 'તો બરાબર, હું પણ ઘર છોડીને જઈ રહી છું!' માણસ: 'તો હું ક્યાં જાઉં?'"
        ],
        'agri_intro': "🌾 કૃષિ અને સરકારી યોજનાઓ",
        'agri_content': "કૃષિ એ છોડ અને પશુધનની ખેતીનું વિજ્ઞાન અને વ્યવહાર છે. ખેડૂતોને મદદ કરતી કેટલીક મુખ્ય સરકારી યોજનાઓ અહીં આપેલી છે:\n\n - **પ્રધાન મંત્રી કિસાન સન્માન નિધિ (PM-KISAN)**: ખેડૂતો માટે એક આવક સહાય યોજના.\n લિંક: https://pmkisan.gov.in/\n\n - **પ્રધાન મંત્રી ફસલ બીમા યોજના (PMFBY)**: ખેડૂતોને નુકસાનથી બચાવવા માટે એક પાક વીમા યોજના.\n લિંક: https://pmfby.gov.in/\n\n - **કિસાન ક્રેડિટ કાર્ડ (KCC)**: ખેડૂતોને સમયસર ધિરાણ પૂરું પાડવાની એક યોજના.\n લિંક: https://www.india.gov.in/schemes-kisan-credit-card-scheme\n\n - **પ્રધાન મંત્રી કૃષિ સિંચાઈ યોજના (PMKSY)**: દેશના દરેક ખેતરને સુનિશ્ચિત સિંચાઈ પૂરી પાડવાનો હેતુ ધરાવે છે.\n લિંક: https://pmksy.gov.in/\n\n - **ગોબરધન (GOBARdhan) યોજના**: ગ્રામીણ વિસ્તારો માટે 'કચરામાંથી સંપત્તિ'ની પહેલ, જેમાં ઘન કચરા અને પશુઓના ગોબરને બાયોગેસ અને જૈવિક ખાતર જેવા ઉપયોગી સંસાધનોમાં રૂપાંતરિત કરવામાં આવે છે.\n લિંક: https://sbm.gov.in/gbdhn/index",
        'health_intro': "🏥 આરોગ્ય સલાહ અને યોજનાઓ",
        'health_content': "તમે આરોગ્ય સલાહ કેવી રીતે મેળવી શકો છો અને સરકારી આરોગ્ય યોજનાઓ વિશેની માહિતી અહીં આપેલી છે:\n\n - **eSanjeevani**: ભારત સરકારની એક રાષ્ટ્રીય ટેલિમેડિસિન સેવા જે મફત ઓનલાઇન ડોક્ટર સલાહ પૂરી પાડે છે.\n લિંક: https://esanjeevani.mohfw.gov.in/\n\n - **આયુષ્માન ભારત - પ્રધાન મંત્રી જન આરોગ્ય યોજના (PM-JAY)**: વિશ્વની સૌથી મોટી આરોગ્ય ખાતરી યોજના જે ગરીબ અને સંવેદનશીલ પરિવારો માટે પ્રતિ વર્ષ પ્રતિ પરિવાર ₹5 લાખનું આરોગ્ય કવર પૂરું પાડે છે.\n લિંક: https://nha.gov.in/PM-JAY",
        'sanitation_intro': "🚽 સ્વચ્છતા જાગૃતિ",
        'sanitation_content': "સમુદાયના આરોગ્ય માટે સ્વચ્છતા જાગૃતિ ખૂબ જ મહત્વપૂર્ણ છે. ભારત સરકારે સ્વચ્છતા અને સ્વચ્છતાને પ્રોત્સાહન આપવા માટે એક વિશાળ ઝુંબેશ શરૂ કરી છે.\n\n - **સ્વચ્છ ભારત મિશન (SBM)**: ખુલ્લામાં શૌચને નાબૂદ કરવા અને ઘન કચરા વ્યવસ્થાપનમાં સુધારો કરવા માટેનો દેશવ્યાપી કાર્યક્રમ. તે ગ્રામીણ અને શહેરી બંને વિસ્તારોમાં શૌચાલય બનાવવા માટે નાણાકીય સહાય પૂરી પાડે છે.\n લિંક: https://swachhbharatmission.gov.in/\n\n - **રાષ્ટ્રીય આરોગ્ય મિશન (NHM) ની ભૂમિકા**: NHM આરોગ્ય પરિણામો સુધારવા પર ધ્યાન કેન્દ્રિત કરે છે, જે સીધા સ્વચ્છતા અને સ્વચ્છતા સાથે જોડાયેલા છે. તે રોગોને અટકાવવા માટે સ્વસ્થ સ્વચ્છતા પ્રથાઓ વિશે જાગૃતિ લાવવાનું કામ કરે છે.",
        'skills_intro': "🎓 કૌશલ્યો અને શિક્ષણ",
        'skills_content': "વ્યક્તિગત વિકાસ અને રાષ્ટ્રીય પ્રગતિ માટે કૌશલ્ય વિકાસ અને શિક્ષણ આવશ્યક છે. અહીં કેટલીક મુખ્ય સરકારી પહેલ આપેલી છે:\n\n - **પ્રધાન મંત્રી કૌશલ વિકાસ યોજના (PMKVY)**: ભારતીય યુવાનોની મોટી સંખ્યાને ઉદ્યોગ-સંબંધિત કૌશલ્ય તાલીમ લેવા સક્ષમ બનાવવાની મુખ્ય યોજના જેથી તેઓ વધુ સારી આજીવિકા સુરક્ષિત કરી શકે.\n લિંક: https://pmkvyofficial.org/\n\n - **રાષ્ટ્રીય શિક્ષણ નીતિ (NEP) 2020**: ભારતની શિક્ષણ પ્રણાલીને રૂપાંતરિત કરવાના ઉદ્દેશ્ય સાથેની એક વ્યાપક નીતિ. તે નાની ઉંમરથી જ વ્યવસાયિક અને કૌશલ્ય-આધારિત શિક્ષણને મુખ્ય પ્રવાહના અભ્યાસક્રમમાં એકીકૃત કરે છે.\n લિંક: https://www.education.gov.in/nep",
        'digital_india_intro': "🇮🇳 ડિજિટલ ઇન્ડિયા",
        'digital_india_content': "ડિજિટલ ઇન્ડિયા કાર્યક્રમનો ઉદ્દેશ ભારતને ડિજિટલ રીતે સશક્ત સમાજ અને જ્ઞાન અર્થતંત્રમાં રૂપાંતરિત કરવાનો છે. મુખ્ય પહેલોમાં શામેલ છે:\n\n - **ડિજી લોકર (DigiLocker)**: નાગરિકોને તેમના સત્તાવાર દસ્તાવેજોને સુરક્ષિત રીતે સંગ્રહિત કરવા અને ઍક્સેસ કરવા માટે એક ડિજિટલ જગ્યા પૂરી પાડે છે.\n - **ભારતનેટ (BharatNet)**: તમામ ગ્રામ પંચાયતોને હાઇ-સ્પીડ ઇન્ટરનેટ કનેક્ટિવિટી પૂરી પાડવાનો હેતુ ધરાવે છે.",
        'make_in_india_intro': "🇮🇳 મેક ઇન ઇન્ડિયા",
        'make_in_india_content': "'મેક ઇન ઇન્ડિયા' પહેલ કંપનીઓને ભારતમાં તેમના ઉત્પાદનોનું ઉત્પાદન કરવા માટે પ્રોત્સાહિત કરે છે. તેનો ઉદ્દેશ આર્થિક વિકાસને વેગ આપવા, નોકરીઓનું સર્જન કરવા અને વિદેશી રોકાણ આકર્ષવાનો છે.",
        'emergency_intro': "🚨 કટોકટી અને હેલ્પલાઇન સપોર્ટ",
        'emergency_content': "કટોકટીના કિસ્સામાં, તમે આ હેલ્પલાઇન નંબરોનો ઉપયોગ કરી શકો છો:\n\n - **ઓલ-ઇન-વન કટોકટી નંબર**: **112** (પોલીસ, ફાયર, એમ્બ્યુલન્સ)\n - **પોલીસ**: **100**\n - **ફાયર**: **101**\n - **એમ્બ્યુલન્સ**: **108**\n - **આપત્તિ વ્યવસ્થાપન**: **1078**\n - **મહિલા હેલ્પલાઇન**: **1091**\n - **કિસાન કોલ સેન્ટર (ખેડૂતો માટે)**: **1800-180-1551**",
        'creator': "આ ચેટબોટ અનુપ યાદવ (બીબીડી યુનિવર્સિટીના વિદ્યાર્થી, નિવાસી સિવાન, બિહાર) દ્વારા બનાવવામાં આવ્યો છે અને પ્રોગ્રામિંગ અંકિત સિંહ દ્વારા કરવામાં આવ્યું છે.",
        'log_message': "વપરાશકર્તાનો પ્રશ્ન લોગ થયો."
    }
}


class ChatbotGUI:
    # --- UI Configuration Constants ---
    BG_COLOR = "#F0F0F0"  # Light Gray
    TEXT_COLOR = "#1C1C1C"  # Near Black
    BOT_BG_COLOR = "#FFFFFF"  # White
    USER_BG_COLOR = "#DCF8C6"  # Light Green
    BUTTON_BG_COLOR = "#007AFF"  # Apple Blue
    BUTTON_FG_COLOR = "#FFFFFF"  # White
    FONT_FAMILY = "Helvetica"
    FONT_NORMAL = (FONT_FAMILY, 12)
    FONT_BOLD = (FONT_FAMILY, 12, "bold")

    def __init__(self, master):
        self.master = master
        self.master.title("Digital Literacy Chatbot")
        self.master.geometry("800x650")
        self.master.configure(bg=self.BG_COLOR)

        # --- State and Data ---
        self.current_lang = 'en'
        self.state = "initial"
        self.quiz_score = 0
        self.quiz_question_num = 0
        
        # --- Command Dispatcher ---
        # Using a dictionary for commands is more scalable than a long if/elif chain
        self.commands = {
            'info': self._show_info,
            'security': self._show_security,
            'quiz': self.start_quiz,
            'agri': self._show_agri,
            'health': self._show_health,
            'skills': self._show_skills,
            'sanitation': self._show_sanitation,
            'emergency': self._show_emergency,
            'digital_india': self._show_digital_india,
            'make_in_india': self._show_make_in_india,
            'time': self._show_time,
            'date': self._show_date,
            'weather': self._show_weather,
            'joke': self._show_joke,
            'image': self._start_image_prompt,
            'creator': self._show_creator,
        }
        
        self._setup_language_selection()

    def _setup_language_selection(self):
        """Creates the initial screen for language selection using a grid layout."""
        self.language_frame = tk.Frame(self.master, bg=self.BG_COLOR, padx=20, pady=20)
        self.language_frame.pack(fill=tk.BOTH, expand=True)

        lang_label = tk.Label(self.language_frame, text="Please select a language:", 
                              font=(self.FONT_FAMILY, 18, "bold"), bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        lang_label.pack(pady=(50, 30))

        # Buttons frame for better layout control
        buttons_frame = tk.Frame(self.language_frame, bg=self.BG_COLOR)
        buttons_frame.pack()

        # Place buttons in a grid
        row, col = 0, 0
        for lang_code, data in LANG_DATA.items():
            btn = tk.Button(buttons_frame, text=data['lang_desc'], font=self.FONT_NORMAL,
                            bg=self.BUTTON_BG_COLOR, fg=self.BUTTON_FG_COLOR, bd=0, 
                            padx=20, pady=10, relief=tk.FLAT,
                            command=lambda code=lang_code: self.set_language(code))
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            col += 1
            if col > 1: # Create a 2-column grid
                col = 0
                row += 1

    def set_language(self, lang_code):
        """Sets the application language and transitions to the main chat UI."""
        self.current_lang = lang_code
        self.master.title(LANG_DATA[self.current_lang]['title'])
        self.language_frame.destroy()
        self._setup_main_ui()
        self._display_message("Bot", LANG_DATA[self.current_lang]['welcome'])

    def _setup_main_ui(self):
        """Sets up the main chat window and input area."""
        self._setup_chat_window()
        self._setup_input_area()
        
    def _setup_chat_window(self):
        """Configures the scrolled text widget for displaying chat history."""
        self.chat_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, 
                                                      bg="#E5DDD5", fg=self.TEXT_COLOR, 
                                                      font=self.FONT_NORMAL, bd=0, padx=10, pady=10)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)

        # Configure tags for color-coded messages
        self.chat_display.tag_configure('bot', background=self.BOT_BG_COLOR, lmargin1=10, lmargin2=10, rmargin=80, relief=tk.RAISED, borderwidth=1, wrap='word')
        self.chat_display.tag_configure('user', background=self.USER_BG_COLOR, lmargin1=80, lmargin2=80, rmargin=10, justify='right', relief=tk.RAISED, borderwidth=1, wrap='word')
        self.chat_display.tag_configure('sender', font=self.FONT_BOLD)

    def _setup_input_area(self):
        """Configures the user input field and send button."""
        input_frame = tk.Frame(self.master, bg=self.BG_COLOR)
        input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.user_input = tk.Entry(input_frame, font=self.FONT_NORMAL, bd=1, 
                                   relief=tk.SOLID, bg="white", fg=self.TEXT_COLOR)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        self.user_input.bind("<Return>", self._send_message_event)

        self.send_button = tk.Button(input_frame, text="Send", font=self.FONT_BOLD,
                                     bg=self.BUTTON_BG_COLOR, fg=self.BUTTON_FG_COLOR, bd=0, 
                                     padx=20, pady=8, command=self._send_message)
        self.send_button.pack(side=tk.RIGHT)
        
    def _send_message_event(self, event):
        self._send_message()

    def _send_message(self):
        user_text = self.user_input.get().strip()
        if user_text:
            self._display_message("You", user_text)
            self._process_command(user_text)
            self.user_input.delete(0, tk.END)

    def _display_message(self, sender, message):
        """Displays a message in the chat window with appropriate styling."""
        self.chat_display.config(state=tk.NORMAL)
        
        tag = 'bot' if sender == "Bot" else 'user'
        self.chat_display.insert(tk.END, f"{sender}:\n", ('sender', tag))
        self.chat_display.insert(tk.END, f"{message}\n\n", tag)
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def _process_command(self, command):
        command = command.lower()
        
        # Priority check for OTP warning
        if 'otp' in command:
            self._display_message("Bot", self._lang_get('otp_warning'))
            return

        # Handle multi-step states
        if self.state == "quiz":
            self._handle_quiz(command)
            return
        elif self.state == "image_prompt":
            self._handle_image_generation(command)
            return

        # Use the command dispatcher
        handler = self.commands.get(command)
        if handler:
            handler()
        else:
            self._handle_nlp_response(command)

    def _lang_get(self, key, default=""):
        """Safely gets a string from the language data, preventing KeyErrors."""
        return LANG_DATA[self.current_lang].get(key, default)

    # --- Command Handler Methods ---
    def _show_info(self):
        response = f"{self._lang_get('info_intro')}\n\n{self._lang_get('info_content')}"
        self._display_message("Bot", response)
        self._log_user_question('info', response)

    def _show_security(self):
        response = f"{self._lang_get('security_tips')}\n\n{self._lang_get('security_content')}"
        self._display_message("Bot", response)
        self._log_user_question('security', response)
    
    def _show_agri(self):
        response = f"{self._lang_get('agri_intro')}\n\n{self._lang_get('agri_content')}"
        self._display_message("Bot", response)
        self._log_user_question('agri', response)

    def _show_health(self):
        response = f"{self._lang_get('health_intro')}\n\n{self._lang_get('health_content')}"
        self._display_message("Bot", response)
        self._log_user_question('health', response)
        
    def _show_skills(self):
        response = f"{self._lang_get('skills_intro')}\n\n{self._lang_get('skills_content')}"
        self._display_message("Bot", response)
        self._log_user_question('skills', response)

    def _show_sanitation(self):
        response = f"{self._lang_get('sanitation_intro')}\n\n{self._lang_get('sanitation_content')}"
        self._display_message("Bot", response)
        self._log_user_question('sanitation', response)

    def _show_emergency(self):
        response = f"{self._lang_get('emergency_intro')}\n\n{self._lang_get('emergency_content')}"
        self._display_message("Bot", response)
        self._log_user_question('emergency', response)

    def _show_digital_india(self):
        response = f"{self._lang_get('digital_india_intro')}\n\n{self._lang_get('digital_india_content')}"
        self._display_message("Bot", response)
        self._log_user_question('digital_india', response)

    def _show_make_in_india(self):
        response = f"{self._lang_get('make_in_india_intro')}\n\n{self._lang_get('make_in_india_content')}"
        self._display_message("Bot", response)
        self._log_user_question('make_in_india', response)
        
    def _show_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        response = f"{self._lang_get('time')}{current_time}"
        self._display_message("Bot", response)
        self._log_user_question('time', response)

    def _show_date(self):
        now = datetime.datetime.now()
        current_date = now.strftime("%A, %B %d, %Y")
        response = f"{self._lang_get('date')}{current_date}"
        self._display_message("Bot", response)
        self._log_user_question('date', response)
        
    def _show_weather(self):
        now = datetime.datetime.now()
        hour, month = now.hour, now.month
        
        weather_desc = ""
        if month in [3, 4, 5, 6, 7, 8]:  # Summer/Monsoon
            weather_desc = "Hot and humid with a chance of rain." if 6 <= hour < 18 else "Warm and clear."
        else:  # Winter
            weather_desc = "Cool and pleasant." if 6 <= hour < 18 else "Cold with a clear sky."

        response = self._lang_get('weather').format(weather_desc=weather_desc)
        self._display_message("Bot", response)
        self._log_user_question('weather', response)

    def _show_joke(self):
        jokes = self._lang_get('jokes', ["Sorry, I'm out of jokes right now."])
        response = f"{self._lang_get('joke_intro')}\n{random.choice(jokes)}"
        self._display_message("Bot", response)
        self._log_user_question('joke', response)
        
    def _start_image_prompt(self):
        self.state = "image_prompt"
        response = self._lang_get('image_prompt')
        self._display_message("Bot", response)
        
    def _show_creator(self):
        response = self._lang_get('creator')
        self._display_message("Bot", response)
        self._log_user_question('creator', response)

    def _handle_nlp_response(self, text):
        try:
            blob = TextBlob(text)
            if self.current_lang != 'en':
                blob = blob.translate(from_lang=self.current_lang, to='en')
            
            polarity = blob.sentiment.polarity
            if polarity > 0.2:
                response = self._lang_get('nlp_positive')
            elif polarity < -0.2:
                response = self._lang_get('nlp_negative')
            else:
                response = self._lang_get('nlp_neutral')
        except Exception:
            response = self._lang_get('unknown_command')
        
        self._display_message("Bot", response)
        self._log_user_question(text, response)

    # --- Quiz Logic ---
    def start_quiz(self):
        self.state = "quiz"
        self.quiz_score = 0
        self.quiz_question_num = 1
        self._display_message("Bot", self._lang_get('quiz_intro'))
        self._ask_quiz_question()

    def _ask_quiz_question(self):
        q_num = self.quiz_question_num
        question = self._lang_get(f'q{q_num}')
        options = self._lang_get(f'q{q_num}_options')
        self._display_message("Bot", f"{question}\n{options}")
        
    def _handle_quiz(self, user_input):
        q_num = self.quiz_question_num
        correct_answer = self._lang_get(f'q{q_num}_ans')

        if user_input.lower() == correct_answer:
            self.quiz_score += 1
            self._display_message("Bot", self._lang_get('correct'))
        else:
            response = f"{self._lang_get('incorrect')} {correct_answer.upper()}"
            self._display_message("Bot", response)
        
        self.quiz_question_num += 1

        if self.quiz_question_num <= 5:
            self._ask_quiz_question()
        else:
            self._end_quiz()

    def _end_quiz(self):
        total_questions = 5
        score_percentage = (self.quiz_score / total_questions) * 100
        
        if score_percentage >= 80:
            result_message = self._lang_get('quiz_end_excellent')
        elif score_percentage >= 50:
            result_message = self._lang_get('quiz_end_good')
        else:
            result_message = self._lang_get('quiz_end_average')

        response = f"{self._lang_get('your_score')}{self.quiz_score}/{total_questions}\n{result_message}"
        self._display_message("Bot", response)
        self.state = "initial"
        self._log_user_question("quiz completion", f"Score: {self.quiz_score}/{total_questions}")

    # --- Image Generation Logic ---
    def _handle_image_generation(self, prompt):
        if not prompt:
            self._display_message("Bot", "Please provide a valid description.")
            return

        # Simulate image generation
        self._display_message("Bot", self._lang_get('image_generating').format(prompt=prompt))
        
        # This is a dummy URL.
        image_url = "https://dummyimage.com/600x400/000/fff&text=" + prompt.replace(" ", "+")
        
        response = f"{self._lang_get('image_link')}{image_url}"
        self._display_message("Bot", response)
        self.state = "initial"
        self._log_user_question(f"generate image: {prompt}", f"generated link: {image_url}")

    # --- Logging ---
    def _log_user_question(self, user_text, bot_response):
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_query": user_text,
            "bot_response": bot_response,
            "language": self.current_lang
        }
        
        try:
            try:
                with open("chat_log.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []
            
            data.append(log_entry)
            
            with open("chat_log.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                
        except IOError as e:
            print(f"Error logging to file: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
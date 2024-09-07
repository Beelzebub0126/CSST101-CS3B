# CSST101-CS3B

Machine Problem No. 1
1. Research and Comprehend:
Introduction to AI
Artificial intelligence (AI) involves the theory and practice of designing computer systems that can learn from and identify patterns in data. These systems use algorithms and models to perform tasks typically associated with human intelligence, such as speech and image recognition, as well as decision-making. AI is built on techniques like machine learning and neural networks, and it also encompasses advanced concepts like deep learning and natural language processing.

AI works by following these five steps:  Input, Processing, Outcomes, Adjustments, and Assessments.

Input
Data is initially gathered from various sources, including text, audio, videos, and more. This data is then categorized into those that are readable by algorithms and those that are not. Protocols and criteria are established to determine which data will be processed and utilized for specific outcomes.
Processing
Once the data is collected and inputted, the AI system determines how to handle it. The AI analyzes and interprets the data using patterns it has been trained to recognize, filtering through the data until it identifies familiar patterns.
Outcomes
Following processing, the AI uses these patterns to predict outcomes, such as customer behavior and market trends. At this stage, the AI decides whether specific data matches previous patterns, effectively categorizing it as a "pass" or "fail," which in turn influences decision-making.
Adjustments
If a data set is deemed a "fail," the AI learns from this and the process is repeated under different conditions. This might involve adjusting the algorithm's rules or making slight modifications to better align with the current data set. This step may involve revisiting the outcomes stage to better suit the new conditions.
Assessments
In the final step, the AI system evaluates the completed task. It synthesizes insights gained from the data to make predictions based on previous outcomes and adjustments. Feedback from these adjustments can be incorporated into the algorithm before proceeding further.

Representation and manipulation are very important in AI because they allow computers to understand, store, and work with human knowledge. This capability allows AI systems to solve complex problems, make informed decisions, and perform tasks that require a level of intelligence like that of humans.
Overview of Knowledge Representation
Knowledge Representation in AI refers to the way in which artificial intelligence systems store, organize, and utilize knowledge to solve complex problems. It is a crucial aspect of AI, enabling machines to mimic human understanding and reasoning. Knowledge representation involves the creation of data structures and models that can efficiently capture information about the world, making it accessible and usable by AI algorithms for decision-making, inference, and learning.
Logical Representation
Logical representation involves using formal logic systems like propositional and predicate logic to represent knowledge in a structured, precise, and unambiguous way.
Logical representation allows AI systems to perform reasoning by applying rules of inference to derive conclusions from known facts. It is commonly used in applications that require rigorous and consistent decision-making, such as theorem proving and rule-based systems.
Semantic Networks
A semantic network is a graphical representation of knowledge where nodes represent concepts, and edges represent relationships between those concepts.
Semantic networks are used to model hierarchical relationships (like class hierarchies in object-oriented programming) and associative relationships (such as synonymy in natural language processing). They help AI systems understand the connections between different concepts and perform tasks like inference, classification, and ontology mapping.
Frames
Frames are data structures that encapsulate knowledge about objects, situations, or events in a structured format. Each frame contains attributes (slots) and their associated values, which can include default values, constraints, and even procedural knowledge.
Frames are used to represent stereotypical situations or objects, allowing AI systems to make inferences based on the structure and relationships within the frames. For example, a frame for a “car” might include slots for make, model, color, and owner, along with rules for filling in missing information.

2. Hands-On Exploration:
Case Study Selection: IBM Watson for Healthcare
Real-World AI Application:
IBM Watson for Healthcare is a prominent example of a medical diagnosis system that leverages AI to assist healthcare professionals in making more accurate and timely decisions, particularly in complex fields like oncology and genomics.
Knowledge Representation in IBM Watson:
Watson employs a combination of natural language processing (NLP), machine learning models, and structured knowledge bases to represent medical knowledge effectively. Each of these components plays a role in how Watson processes vast amounts of unstructured data and transforms it into actionable insights.
•	NLP: Watson uses NLP to analyze and extract relevant information from unstructured sources such as medical literature, clinical trial data, and patient health records. This enables the system to understand complex medical terminology and connect it with appropriate diagnoses and treatments.
•	Structured Knowledge Bases: Watson organizes the processed data into structured knowledge bases, which serve as a reference for physicians. These knowledge bases are continually updated with the latest medical research, clinical guidelines, and treatment protocols, making them a reliable source for informed decision-making.
•	Machine Learning Models: Through probabilistic reasoning, Watson’s machine learning algorithms analyze patterns in patient data and medical records, allowing the system to make predictions about potential diagnoses or treatment plans. This is especially useful in personalizing treatments for patients with rare diseases or specific genetic profiles.
Effectiveness in Solving Problems:
Watson's effectiveness lies in its ability to process and analyze vast quantities of medical information far more quickly than human doctors, providing real-time insights that can aid in diagnosing diseases and suggesting treatment options. In oncology, for instance, Watson analyzes genetic mutations to identify suitable treatments, a process that would otherwise be time-consuming for human experts. The system is highly adaptable, continuously learning from new data, which is vital in fields like genomics where knowledge evolves rapidly.

Representation Creation
Simple Problem: Identifying Treatment Options for Breast Cancer Patients
In the context of IBM Watson for Healthcare, a common problem is assisting doctors in identifying the most appropriate treatment options for breast cancer patients based on their individual genetic profiles, medical histories, and the latest research.

Knowledge Representation Model: Ontology-Based Semantic Network
To solve this problem, we can create a semantic network that represents relationships between the patient’s clinical data, genetic mutations, possible treatments, and outcomes. In this case, each node represents a key concept, such as a type of breast cancer, a genetic mutation (e.g., BRCA1 or BRCA2), treatment options (chemotherapy, surgery, targeted therapy), and outcomes (survival rates, side effects).
Structure of the Semantic Network:
•	Patient Data Node: Represents the individual patient, including age, medical history, and symptoms.
•	Genetic Mutation Nodes: Capture information about relevant genetic mutations (e.g., BRCA1 mutation).
•	Breast Cancer Type Nodes: Represent different types of breast cancer (e.g., hormone receptor-positive, HER2-positive).
•	Treatment Nodes: Capture various treatment options (e.g., chemotherapy, immunotherapy, surgery).
•	Outcome Nodes: Represent possible outcomes (e.g., remission, recurrence, survival rate).
Example Network Relationships:
•	A patient with a BRCA1 mutation is connected to the Breast Cancer Type node representing HER2-positive breast cancer.
•	The system links this information to treatment options, such as targeted therapy (e.g., trastuzumab), which is effective for HER2-positive patients.
•	The system further connects treatment options to outcome nodes, showing survival rates, potential side effects, and risks.

Diagram of the Semantic Network
To visualize this, you can create a diagram with nodes representing each element (patient, genetic mutation, treatment, outcome) and edges representing relationships between them.












How the AI System Utilizes It:
Watson analyzes patient data and navigates this semantic network to:
1.	Identify Relevant Information: The system reviews patient records, identifies relevant genetic mutations, and connects them to possible breast cancer types.
2.	Recommend Treatment: Based on the relationships in the semantic network, the system suggests treatments that have been effective for other patients with similar profiles.
3.	Predict Outcomes: Watson uses past data and clinical studies to predict the most likely outcomes for the selected treatment, helping doctors choose the best course of action for their patient.
This semantic network allows Watson to represent complex medical relationships and deliver personalized, data-driven treatment recommendations for patients.





References: 
https://www.coursera.org/articles/how-does-ai-work
https://www.geeksforgeeks.org/knowledge-representation-in-ai/
https://wearecommunity.io/communities/healthcare/articles/5012
https://healthcare-digital.com/technology-and-ai/four-ways-which-watson-transforming-healthcare-sector


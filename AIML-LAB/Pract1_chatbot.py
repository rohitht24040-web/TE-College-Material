#Name : Hajare Rohit Siddhinath
#Class: SE - ITA
#Rollno : TIA30
#Practical 1. Title: Intelligent Agents and PEAS Representation

# ============================================================
# PR1: Intelligent Agents and PEAS Representation
# Application: Health Access Intelligent Agent
# Type: Simple Rule-Based Intelligent Agent
# ============================================================

# ------------------------------------------------------------
# SENSOR FUNCTION
# ------------------------------------------------------------
# This function simulates sensors by taking information from
# the user as input.
# ------------------------------------------------------------

def get_sensor_data():
    print("\n--- Health Access Agent ---")

    name = input("Enter your name: ")
    query = input("Enter your health-related query: ").lower()

    return {
        "name": name,
        "query": query
    }

# ------------------------------------------------------------
# INTELLIGENT AGENT / DECISION ENGINE
# ------------------------------------------------------------
# The agent analyzes the input and applies predefined rules.
# ------------------------------------------------------------

def health_access_agent(sensor_data):

    name = sensor_data["name"]
    query = sensor_data["query"]

    # Default action
    action = "Please provide more information about your request."

    # Rule 1: Emergency-related request
    if ("chest pain" in query or
        "difficulty breathing" in query or
        "severe bleeding" in query or
        "unconscious" in query):

        action = (
            "Emergency condition detected. "
            "Please seek immediate medical assistance "
            "or contact your local emergency service."
        )

    # Rule 2: Appointment request
    elif ("appointment" in query or
          "book doctor" in query or
          "doctor appointment" in query):

        action = (
            "Appointment request detected. "
            "Please provide your preferred doctor, "
            "date, and time."
        )

    # Rule 3: Doctor information
    elif ("doctor" in query or
          "specialist" in query):

        action = (
            "Doctor information request detected. "
            "Please specify the type of doctor or specialist "
            "you are looking for."
        )

    # Rule 4: Hospital / healthcare facility
    elif ("hospital" in query or
          "clinic" in query or
          "health center" in query or
          "healthcare" in query):

        action = (
            "Healthcare facility request detected. "
            "Please specify your location to find suitable "
            "healthcare assistance."
        )

    # Rule 5: Medicine-related query
    elif ("medicine" in query or
          "medication" in query or
          "prescription" in query):

        action = (
            "Medication-related request detected. "
            "Please consult a qualified healthcare professional "
            "for appropriate medical advice."
        )

    # Rule 6: General health information
    elif ("fever" in query or
          "cough" in query or
          "headache" in query or
          "symptom" in query):

        action = (
            "Health-related symptoms detected. "
            "For proper evaluation and treatment, "
            "please consult a healthcare professional."
        )

    # Rule 7: Greeting
    elif ("hello" in query or
          "hi" in query or
          "hey" in query):

        action = (
            "Hello! I am the Health Access Intelligent Agent. "
            "I can help with basic healthcare access requests "
            "such as appointments, doctors, hospitals, and "
            "health-related assistance."
        )

    return {
        "name": name,
        "query": query,
        "action": action
    }

# ------------------------------------------------------------
# ACTUATOR FUNCTION
# ------------------------------------------------------------
# The actuator performs the action selected by the agent.
# In this simulation, the actuator is the text response.
# ------------------------------------------------------------

def perform_action(agent_result):

    print("\n--- Agent Response ---")
    print("User:", agent_result["name"])
    print("Query:", agent_result["query"])
    print("Action:", agent_result["action"])

# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    print("==============================================")
    print("   HEALTH ACCESS INTELLIGENT AGENT")
    print("   PEAS-Based Rule-Based Agent")
    print("==============================================")

    # Step 1: Read input from virtual sensor
    sensor_data = get_sensor_data()

    # Step 2: Pass sensor data to intelligent agent
    agent_result = health_access_agent(sensor_data)

    # Step 3: Perform action selected by the agent
    perform_action(agent_result)

    print("\n==============================================")
    print("Agent execution completed.")
    print("==============================================")

# ------------------------------------------------------------
# PROGRAM EXECUTION
# ------------------------------------------------------------

if __name__ == "__main__":
    main()


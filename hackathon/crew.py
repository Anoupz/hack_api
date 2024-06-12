import os

import agentops
from agentops import track_agent
from crewai import Agent, Task, Process, Crew
from langchain_groq import ChatGroq
from crewai.project import CrewBase, agent, crew, task

agentops.init()


@CrewBase
class ParseTextCrew:
    agents_config = "crew_config/agents.yaml"
    tasks_config = "crew_config/tasks.yaml"

    def __init__(self):
        self.groq_llm = ChatGroq(
            temperature=0,
            groq_api_key=os.environ.get("GROQ_API_KEY"),
            model_name="llama3-70b-8192",
        )

    @track_agent(name="parse_text_specialist")
    @agent
    def parse_text_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["parse_text_specialist"],
            llm=self.groq_llm,
            allow_delegation=False,
            verbose=False,
        )

    @task
    def parse_text_task(self) -> Task:
        return Task(
            config=self.tasks_config["parse_text_task"],
            agent=self.parse_text_specialist(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.parse_text_specialist(),
            ],
            tasks=[
                self.parse_text_task(),
            ],
            process=Process.sequential,
            memory=False,
            verbose=2,
        )

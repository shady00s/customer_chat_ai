from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

# Uncomment the following line to use an example of a custom tool
# from products_crew.tools.custom_tool import MyCustomTool


# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool
@CrewBase
class ProductsCrew:
    """ProductsCrew crew"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            llm=ChatGroq(
                model="groq/mixtral-8x7b-32768",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            ),
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"],
            verbose=True,
            llm=ChatGroq(
                model="groq/mixtral-8x7b-32768",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            ),
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(config=self.tasks_config["reporting_task"], output_file="report.md")

    @crew
    def crew(self) -> Crew:
        """Creates the ProductsCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

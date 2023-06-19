import click
from langchain.tools import MoveFileTool, format_tool_to_openai_function
from langchain.tools.file_management import (
    ReadFileTool,
    CopyFileTool,
    DeleteFileTool,
    MoveFileTool,
    WriteFileTool,
    ListDirectoryTool,
)
from langchain.agents.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory
from langchain.agents.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.agents import AgentType, initialize_agent


@click.command()
def interact():
    """與OpenAI Functions進行互動"""
    model = ChatOpenAI(model="gpt-3.5-turbo-0613")
    tools = FileManagementToolkit().get_tools()
    open_ai_agent = initialize_agent(tools,
                                     model,
                                     agent=AgentType.OPENAI_FUNCTIONS,
                                     verbose=False)

    while True:
        try:
            question = click.prompt('Question: ')
            tool_result = open_ai_agent.run(question)
            click.echo(f'Answer: {tool_result}')
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    interact()

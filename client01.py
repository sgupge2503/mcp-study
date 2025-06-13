from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio接続用のサーバーパラメータを作成
server_params = StdioServerParameters(
    command="mcp",  # 実行ファイル
    args=["run", "server.py"],  # オプションのコマンドライン引数
    env=None,  # オプションの環境変数
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 接続を初期化
            await session.initialize()

            # List available resources
            resources = await session.list_resources()
            print("LISTING RESOURCES")
            for resource in resources:
                print("Resource: ", resource)

            # List available tools
            tools = await session.list_tools()
            print("LISTING TOOLS")
            for tool in tools.tools:
                print("Tool: ", tool.name)

            # Read a resource
            print("READING RESOURCE")
            content, mime_type = await session.read_resource("greeting://hello")

            # Call a tool
            print("CALL TOOL")
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print(result.content)



if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

    
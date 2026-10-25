"""Real SDK initialization/discovery/invocation against the local stdio subprocess."""

import asyncio
import sys
from pathlib import Path

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ModuleNotFoundError as error:
    raise SystemExit(
        f"Missing MCP dependency: {error.name}. Install the approved dev/MCP environment; "
        "see docs/OFFLINE_SETUP.md#python-runtime. No runtime installation was attempted."
    ) from error


async def main():
    server = str(Path(__file__).with_name("mcp_server.py").resolve())
    async with stdio_client(
        StdioServerParameters(command=sys.executable, args=[server])
    ) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            listing = await session.list_tools()
            assert "list_samples" in {t.name for t in listing.tools}
            result = await session.call_tool("list_samples", {"limit": 1, "split": "train"})
            assert not result.is_error
            assert "s1" in str(result.content)
            bad = await session.call_tool("list_samples", {"limit": 999})
            assert bad.is_error
    print("MCP initialized, discovered tools, checked success and invalid-input error")


if __name__ == "__main__":
    asyncio.run(main())

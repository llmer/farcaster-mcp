
# Farcaster MCP

<p align="center">
<img src="https://i.postimg.cc/JhN2tXm6/og-image.jpg" alt="Farcaster MCP Logo" width="200" height="auto"/>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)

## Overview

This MCP (Model Context Protocol) server leverages the [Warpcast](https://warpcast.com/) API, one of many Farcaster [clients](/a16z/awesome-farcaster#clients) to provide a comprehensive set of tools for interacting with the Farcaster protocol through LLMs like Cursor and Claude . Farcaster is a popular decentralized social media protocol supported on Solana, Ethereum and other EVM compatible networks (e.g. Base, Optimism, Arbitrum e.t.c.).

## Features

- Publish a cast
- Get a cast's information
- Follow and unfollow other users
- Get users' followers and followed users
- Like and unlike a cast
- Recast a cast
- Get your and other users' profile information
- Get Warpcast API status
- Get recent casts and users
- Get channel information
- Get channel followers
- Get channel members
- Get channel blocked members
- And many other features.

## Installation

### Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (Python package installer and environment manager)
- A Farcaster account's 24-word mnemonic passphrase. Which means a Farcaster account is required.

### Option 1: Local Installation

```bash
# Clone the repository
git clone https://github.com/kaiblade/farcaster-mcp.git
cd farcaster-mcp

# Create a virtual environment and install dependencies
uv venv
uv pip install -e .

export MNEMONIC="<your-farcaster-account-mnemonic-passphrase>"

# Run the server
uv run farcaster_mcp.py
```

### Option 2: Docker Installation

```bash
# Clone the repository
git clone https://github.com/kaiblade/farcaster-mcp.git
cd farcaster-mcp

# Build the Docker image
docker build -t farcaster-mcp .

# Run the container
docker run -p 8080:8080 -e MNEMOMIC="<your-farcaster-account-mnemonic-passphrase>" farcaster-mcp
```
## Environment Variables

- `MNEMONIC`: Required. A Farcaster account's 24-word mnemonic passphrase.

## Security Notes

- Never expose your Farcaster account's mnenomic passphrase in the source code
- Use environment variables for sensitive configuration

## Usage

Once the server is running, configure the [Cursor](https://www.cursor.com/downloads) desktop to
connect to the server with:

```json
{
    "mcpServers": {
        "Farcaster-mcp": {
            "url": "http://127.0.0.1:8080/sse"
        }
    }
}
```

Since the MCP server is using the Server-Sent Events (SSE) [transport](https://modelcontextprotocol.io/docs/concepts/transports#built-in-transport-types) instead of the Standard Input/Output (stdio) transport, which Claude desktop only supports, the server won't work with it except through an [MCP proxy](https://github.com/sparfenyuk/mcp-proxy).

### Available Tools
The server exposes several endpoints that can be used to interact with the Farcaster protocol. Below are some of the tools that are exposed:

- `post_cast`: Publish a cast to the farcaster protocol.
- `follow_user`: Follow a user using their Farcaster ID (fid).
- `unfollow_user`: Unfollow a user using their fid.
- `recast`: Recast a cast.
- `like_cast`: Like a cast using its cast hash.
- `delete_cast`: Delete a cast you posted using its cast hash.
- `get_user`: Get a user's profile information using their fid.
- `get_me`: Get your profile information.
- `delete_cast_likes`: Unlike a cast using its fid.
- `get_healthcheck`: Get the status of the Warpcast API.
- `get_channel`: Get a channel's information using its channel ID.
- `get_channel_followers`: Get the list of a channel's followers.
- `get_user_followed_channels`: Using a user's fid, get their followed channels.
- `get_channel_members`: Get the list of channel members.
- `get_channel_banned_users`: Get the list of a channel's banned users.
- `get_channel_blocked_users`: Get the list of a channel's blocked users.
- `get_user`:  Using a user's fid, get their username.

For more possible tools or more information about the exposed tools, check these reference pages:

- https://a16z.github.io/farcaster-py/reference/
- https://docs.farcaster.xyz/reference/warpcast/api

### Example Queries

Here are some example questions you can ask Cursor or Claude once the server is connected:

```
- Post a cast of the current price of Solana in USD
- Get my profile info.
- How many followers does Linda Xie have?
- Get me the most recent Linda Xie's cast and like it.
- List the base channel members and their roles. Get their usernames as well.
- Who is the creator of the base channel?
- Is the API online?
```

## License

MIT License

Copyright (c) 2025 KAIBLADE-FARCASTER-MCP

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

- [Warpcast](https://warpcast.com/) for providing the channel related endpoints through their API.
- [a16z](https://github.com/a16z) for providing the cast and user related endpoints through the `farcaster-py` SDK.

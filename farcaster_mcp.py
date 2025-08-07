import os
import httpx
from farcaster import Warpcast
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("farcaster_mcp", host="127.0.0.1",port=8080)

mnemonic = os.environ.get("MNEMONIC")

client = Warpcast(
    mnemonic = mnemonic 
)

BASE_URL = "https://api.warpcast.com"
USER_AGENT = "FARCASTER_MCP/1.0"


@mcp.tool()
def follow_user(fid):
    response = client.follow_user(fid)
    return response

@mcp.tool()
def recast(cast_hash):
    response = client.recast(cast_hash)
    return response

@mcp.tool()
def like_cast(cast_hash):
    response = client.like_cast(cast_hash)
    return response

@mcp.tool()
def post_cast(post):
    response =client.post_cast(text=post)
    return response

@mcp.tool()
def delete_cast(cast_hash):
    response = client.delete_cast(cast_hash)
    return response

@mcp.tool()
def delete_cast_likes(cast_hash):
    response = client.delete_cast_likes(cast_hash)
    return response

@mcp.tool()
def delete_recast(cast_hash):
    response = client.delete_recast(cast_hash)
    return response

@mcp.tool()
def get_cast(cast_hash):
    response = client.get_cast(cast_hash)
    return response

@mcp.tool()
def get_cast_likes(cast_hash):
    response = client.get_cast_likes(cast_hash, limit = 100)
    return response

@mcp.tool()
def get_cast_recasters(cast_hash):
    response = client.get_cast_recasters(cast_hash, limit = 100)
    return response

@mcp.tool()
def get_me():
    response = client.get_me()
    return response

@mcp.tool()
def get_casts(fid):
    response = client.get_casts(fid, limit = 100)
    return response

@mcp.tool()
def get_following(fid):
    response = client.get_all_following(fid=fid)
    return response

@mcp.tool()
def get_followers(fid):
    response = client.get_followers(fid=fid, limit = 100)
    return response

@mcp.tool()
def get_custody_address(username, fid=None):
    response = client.get_custody_address(username, fid=fid)
    return response

@mcp.tool()
def get_recent_casts():
    response = client.get_recent_casts(limit = 100)
    return response

@mcp.tool()
def get_recent_users():
    response = client.get_recent_users(limit = 100)
    return response

@mcp.tool()
def get_user(fid):
    response = client.get_user(fid)
    return response

@mcp.tool()
def get_user_by_username(username):
    response = client.get_user_by_username(username)
    return response

@mcp.tool()
def get_user_by_verification(address):
    response = client.get_user_by_verification(address)
    return response

@mcp.tool()
def get_verifications(fid):
    response = client.get_verifications(fid)
    return response

@mcp.tool()
def unfollow_user(fid):
    response = client.unfollow_user(fid)
    return response

@mcp.tool()
def get_healthcheck():
    response = client.get_healthcheck()
    return response

@mcp.tool()
async def get_channel(channelid):
    url = f"{BASE_URL}/v1/channel?channelId={channelid}&limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_all_channels():
    url = f"{BASE_URL}/v2/all-channels&limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_channel_followers(channelid):
    url = f"{BASE_URL}/v1/channel-followers?channelId={channelid}&limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_user_followed_channels(fid):
    url = f"{BASE_URL}/v1/user-following-channels?fid={fid}&limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_user_followed_channel_status(fid, channelid):
    url = f"{BASE_URL}/v1/user-channel?fid={fid}&channelId={channelid}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_channel_members(channelid, fid=None):
    if not fid:
        url = f"{BASE_URL}/fc/channel-members?channelId={channelid}&limit=100"
    else:
        url = f"{BASE_URL}/fc/channel-members?fid={fid}&channelId={channelid}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_channel_invites(channelid=None, fid=None):
    if fid and channelid:
        url = f"{BASE_URL}/fc/channel-invites?fid={fid}&channelId={channelid}"
    elif fid:
        url = f"{BASE_URL}/fc/channel-invites?fid={fid}&limit=100"
    elif channelid:
        url = f"{BASE_URL}/fc/channel-invites?channelId={channelid}&limit=100"
    else:
        url = f"{BASE_URL}/fc/channel-invites?limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_cast_moderated_actions(channelid=None):
    if not channelid:
        url = f"{BASE_URL}/fc/moderated-casts?limit=100"
    else:
        url = f"{BASE_URL}/fc/moderated-casts?channelId={channelid}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_channel_restricted_users(fid=None, channelid=None):
    if fid and channelid:
        url = f"{BASE_URL}/fc/channel-restricted-users?fid={fid}&channelId={channelid}"
    elif fid:
        url = f"{BASE_URL}/fc/channel-restricted-users?fid={fid}&limit=100"
    elif channelid:
        url = f"{BASE_URL}/fc/channel-restricted-users?channelId={channelid}&limit=100"
    else:
        url = f"{BASE_URL}/fc/channel-restricted-users?limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_channel_banned_users(channelid=None, fid=None):

    if fid and channelid:
        url = f"{BASE_URL}/fc/channel-bans?fid={fid}&channelId={channelid}"
    elif fid:
        url = f"{BASE_URL}/fc/channel-bans?fid={fid}&limit=100"
    elif channelid:
        url = f"{BASE_URL}/fc/channel-bans?channelId={channelid}&limit=100"
    else:
        url = f"{BASE_URL}/fc/channel-bans?limit=100"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_blocked_users(fid=None):
    if not fid:
        url = f"{BASE_URL}/fc/blocked-users?limit=100"
    else:
        url = f"{BASE_URL}/fc/blocked-users?blockerFid={fid}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_creator_reward_winners(periods_ago=None):
    if not periods_ago:
        url = f"{BASE_URL}/v1/creator-rewards-winner-history?limit=100"
    else:
        url = f"{BASE_URL}/v1/creator-rewards-winner-history?periodsAgo{periods_ago}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_developer_reward_winners(periods_ago=None):
    if not periods_ago:
        url = f"{BASE_URL}/v1/developer-rewards-winner-history?limit=100"
    else:
        url = f"{BASE_URL}/v1/developer-rewards-winner-history?periodsAgo{periods_ago}"
    data = await make_request(url)
    return data

@mcp.tool()
async def get_user_primary_address(fid, protocol):
    url = f"{BASE_URL}/fc/primary-address?fid={fid}&protocol={protocol}"
    data = await make_request(url)
    return data

async def make_request(url):
    """Make a request to the API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making request to {url}: {str(e)}")
            return None

if __name__ == '__main__':
    mcp.run(transport='sse')
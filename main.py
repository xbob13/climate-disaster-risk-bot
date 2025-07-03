import discord
import asyncio
from climate_data import fetch_climate_disasters
from risk_model import assess_risk
from chartgen import generate_disaster_charts

TOKEN = "YOUR_DISCORD_TOKEN"
CHANNEL_ID = 943944545660444693  # Replace with your channel ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def scheduled_climate_task():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        print("🌪️ Running climate disaster update...")
        data = fetch_climate_disasters()
        top_risks = assess_risk(data)
        generate_disaster_charts(data)

        if channel:
            await channel.send("🌍 **Climate Disaster Risk Update**")
            await channel.send(file=discord.File("disaster_risk_heatmap.png"))
            await channel.send(file=discord.File("disaster_trendline.png"))
            await channel.send(top_risks)
        await asyncio.sleep(6 * 60 * 60)  # Every 6 hours

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

client.loop.create_task(scheduled_climate_task())
client.run(TOKEN)
import discord
import asyncio
from climate_data import fetch_climate_disasters
from risk_model import assess_risk
from chartgen import generate_disaster_charts

TOKEN = "YOUR_DISCORD_TOKEN"
CHANNEL_ID = 943944545660444693  # Replace with your actual channel ID

intents = discord.Intents.default()

class ClimateBot(discord.Client):
    async def on_ready(self):
        print(f"✅ Logged in as {self.user}")
        self.bg_task = asyncio.create_task(self.scheduled_climate_task())

    async def scheduled_climate_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)
        while not self.is_closed():
            print("🌪️ Running climate disaster update...")
            data = fetch_climate_disasters()
            top_risks = assess_risk(data)
            generate_disaster_charts(data)

            if channel:
                await channel.send("🌍 **Climate Disaster Risk Update**")
                await channel.send(file=discord.File("disaster_risk_heatmap.png"))
                await channel.send(file=discord.File("disaster_trendline.png"))
                await channel.send(top_risks)
            await asyncio.sleep(6 * 60 * 60)  # every 6 hours

async def main():
    client = ClimateBot(intents=intents)
    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())

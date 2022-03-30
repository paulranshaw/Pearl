import discord
from discord.ext import commands

class Disonnect(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    async def cleanup(self, guild): #Method to cleanup so that Pearl is ready for future instances.
        try: #Disconnect from the current voice state.
            await guild.voice_client.disconnect() 
        except AttributeError:
            pass

    #Disconnect command to make Pearl leave a voice channel.
    @commands.command()
    @commands.guild_only() #Validating usage to within guild only.
    @commands.has_permissions(administrator=True) #Validating command author has guild administrator permission.
    async def disconnect(self, ctx, *, channel: discord.VoiceChannel=None):
        await ctx.message.delete() #Delete command message.
        if not ctx.author.voice: #Return if command author is not in a voice channel and should not be interfering with unsuspecting people!
            return
        vc = ctx.voice_client
        if not vc or not vc.is_connected(): #Return if Pearl does not currently have a voice state instance to cleanup.
            return
        await self.cleanup(ctx.guild)

def setup(bot):
    bot.add_cog(Disonnect(bot))
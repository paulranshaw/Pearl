import discord
from discord.ext import commands

class Connect(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot
    
    #Connect command to make Pearl join a voice channel.
    @commands.command()
    @commands.guild_only() #Validating usage to within guild only.
    @commands.has_permissions(administrator=True) #Validating command author has guild administrator permission.
    async def connect(self, ctx, *, channel: discord.VoiceChannel=None):
        await ctx.message.delete() #Delete command message.
        if not ctx.author.voice: #Return if command author is not in a voice channel and should not be interfering with unsuspecting people!
            return
        if not channel: #If a channel is not passed as an arg, try set the channel to that of the command author.
            try:
                channel = ctx.author.voice.channel
            except:
                pass
        vc = ctx.voice_client
        if vc: #If Pearl is already within a voice channel and vc state is current, try move Pearl to the newly requested channel.
            if vc.channel.id == channel.id:
                return
            try:
                await vc.move_to(channel)
            except:
                pass
        else:
            try:
                await channel.connect() #Connecting Pearl to the requested channel.
            except:
                pass

def setup(bot):
    bot.add_cog(Connect(bot))
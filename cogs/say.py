from discord.ext import commands

class Say(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    #Say command to take message content from command author to then output said message content from Pearl.
    @commands.command()
    @commands.guild_only() #Validating usage to within guild only.
    @commands.has_permissions(administrator=True) #Ensuring command author has guild administrator permission.
    async def say(self, ctx, *, content):
        await ctx.message.delete() #Delete the command message.
        await ctx.send(content) #Output message content from Pearl.

def setup(bot):
    bot.add_cog(Say(bot))
import discord
import random
from discord.ext import commands

PHRASES = [ #Collection of phrases to output.
    'Do you think I\'m purrfect? :innocent:',
    'Is someone talking about me? <:pearlhyper:898219733613170708>',
    'Hey human, I\'m hungry why don\'t you feed me already! :poultry_leg:', 
    'Just seen a bird, must hunt! :bird:',
    'What do you want? I\'m trying to :zzz:',
    'Worship me, your true leader! <:pearl:887492285724520449>'
    ]

REACTIONS = [ #Collection of reactions to react with.
    ':drpearl:898224818602774548',
    ':pearl:887492285724520449',
    ':pearlhyper:898219733613170708',
    'pearlpog:953095702320406539',
    ':pearlpop:905846621152108684'
    ]

class on_Message(commands.Cog):

    def __innit__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #Upon message being sent.
    async def on_message(self, msg):
        if msg.author.bot:
            return                                
        if discord.utils.get(msg.guild.members, id=000000000000000000) in msg.mentions: #If Pearl is mentioned. Replace 0s with bot user ID.
            return await msg.channel.send(random.choice(PHRASES))
        elif 'pearl' in msg.content.lower(): #If content is within message then react.
            await msg.add_reaction(random.choice(REACTIONS))
        else:
            return

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(on_Message(bot))
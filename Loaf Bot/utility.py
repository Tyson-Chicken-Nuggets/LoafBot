import discord
import sqlite3
from discord.ext import commands
from utils import *
class Utility:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def server(self, ctx):
		"""sends an invite to the support server"""
		await ctx.send('Join the support server at {}'.format('https://discord.gg/uJR4rcW'))

	@commands.command()
	async def invite(self, ctx):
		"""sends the OAuth2 URL used for adding the bot to a server"""
		oauth2 = 'https://discordapp.com/api/oauth2/authorize?client_id=430438798141423617&permissions=334883910&scope=bot'
		await ctx.send('Add the bot to your server using {}'.format(oauth2))


	@commands.command()
	async def roles(self, ctx, user : discord.Member = None):
		"""sends the list of roles for the server, or for the specified user, along with their IDs"""
		if user == None:
			object = ctx.guild.name
			convoker = ctx.message.author
			rolelist = ''
			counter = 0
			wrap = 0
			for role in ctx.guild.roles:
				if wrap < 21:
					rolelist += str(role.id)
					rolelist += '	---   '
					rolelist += role.name
					rolelist += '\n'
					counter += 1
					wrap += 1
				else:
					em = discord.Embed(title = f'Roles for **{object}**:' , description = rolelist, colour = 0x4cff30)
					em.set_author(name=convoker.display_name, icon_url=convoker.avatar_url)	
					await ctx.send(embed=em)
					wrap = 0

					rolelist = ''

					rolelist += str(role.id)
					rolelist += '	---   '
					rolelist += role.name
					rolelist += '\n'
					counter += 1
					wrap += 1
		else:
			object = user.display_name
			convoker = user
			rolelist = ''
			counter = 0
			wrap = 0
			for role in user.roles:
				if wrap < 21:
					rolelist += str(role.id)
					rolelist += '	---   '
					rolelist += role.name
					rolelist += '\n'
					counter += 1
					wrap += 1
				else:
					em = discord.Embed(title = f'Roles for **{object}**:' , description = rolelist, colour = 0x4cff30)
					em.set_author(name=convoker.display_name, icon_url=convoker.avatar_url)	
					await ctx.send(embed=em)
					wrap = 0

					rolelist = ''

					rolelist += str(role.id)
					rolelist += '	---   '
					rolelist += role.name
					rolelist += '\n'
					counter += 1
					wrap += 1

		rolelist += '\n **'
		rolelist += str(counter)
		rolelist += ' roles**'

		em = discord.Embed(title = f'Roles for **{object}**:' , description = rolelist, colour = 0x4cff30)
		em.set_author(name=convoker.display_name, icon_url=convoker.avatar_url)	
		await ctx.send(embed=em)

	@commands.command()
	async def prefix(self, ctx):
		"""shows the custom prefix for this server"""
		try:
			prefix = self.bot.prefixes[ctx.message.guild.id]
			await ctx.send(f'The custom prefix for this server is `{prefix}`')
		except:
			await ctx.send('The prefix for this server is `>`')

def setup(bot):
    bot.add_cog(Utility(bot))

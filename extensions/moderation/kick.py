from settings import *


class kick(ezcord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="[MODERATOR] Kick a user from the server")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, reason: discord.Option(str, required=False)):
        await ctx.defer()
        # Check, so the user cannot ban themselves or the bot
        if user == ctx.author:
            error_embed = ezcord.TEmbed("error_embed", error="You cannot kick yourself!", color=embed_color)
            error_embed.set_footer(text=footer)
            await ctx.respond(embed=error_embed)
        if user == self.bot.user:
            error_embed = ezcord.TEmbed("error_embed", error="You cannot kick me!", color=embed_color)
            error_embed.set_footer(text=footer)
            await ctx.respond(embed=error_embed)

        # Send the user a DM (if enabled in settings)
        if mod_user_dm:
            dm_embed = ezcord.TEmbed("dm_embed", guild=ctx.guild.name, moderator=ctx.author.mention, reason=reason, color=embed_color)
            dm_embed.set_footer(text=footer)
            try:
                await user.send(embed=dm_embed)
            except discord.Forbidden:
                pass

        # Ban the user
        try:
            await user.ban(reason=reason)
            success_embed = ezcord.TEmbed("kick_success_embed", user=user.mention, reason=reason, color=embed_color)
            success_embed.set_footer(text=footer)
            await ctx.respond(embed=success_embed)
        except discord.Forbidden:
            error_embed = ezcord.TEmbed("error_embed", error="I do not have the required permissions to kick this user!", color=embed_color)
            error_embed.set_footer(text=footer)
            await ctx.respond(embed=error_embed)
            return
        
        # Log the action (if enabled in settings)
        if mod_log:
            log_embed = ezcord.TEmbed("kick_log_embed", user=user, moderator=ctx.author, reason=reason, color=embed_color)
            log_embed.set_footer(text=footer)
            log_channel = ctx.guild.get_channel(mod_log_channel)
            await log_channel.send(embed=log_embed)
        
        
def setup(bot):
    bot.add_cog(kick(bot))

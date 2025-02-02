from .base import BaseSummaryCommand

class LinkSummaryCommand(BaseSummaryCommand):
    async def execute(self, from_link: str, to_link: str):
        """Execute link summary command"""
        try:
            # Send initial response
            await self.interaction.response.defer(thinking=True, ephemeral=True)
            
            start_id = self.message_service.extract_message_id(from_link)
            end_id = self.message_service.extract_message_id(to_link)
            
            if not start_id or not end_id:
                await self.send_status("Neplatné odkazy na zprávy. Použijte prosím platné odkazy na Discord zprávy.")
                return
                
            await self.send_status("Načítám zprávy ve vybraném rozsahu...")
            
            messages = await self.message_service.get_messages_between(
                self.ctx.channel, start_id, end_id
            )
            
            await self.send_summary(messages, "Shrnutí zpráv ve vybraném rozsahu")
            
        except Exception as e:
            await self.send_status(f"Chyba při zpracování příkazu: {str(e)}")
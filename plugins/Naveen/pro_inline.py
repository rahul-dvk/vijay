from pyrogram import Client
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent 

@Client.on_inline_query()
async def inlinemode(bot, query: InlineQuery):
    await query.answer(
        results=[

            InlineQueryResultArticle(
                title="Naveen",
                description="Click Here",
                thumb_url="https://telegra.ph/file/a91ddf16775ec8ef0bd9e.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Owner of the Bot"""
                )
            ),

            InlineQueryResultArticle(
                title="About the Bot",
                description="Show the Details of the Bot and Show the Purpose of Vijay BoT",
                thumb_url="https://telegra.ph/file/a91ddf16775ec8ef0bd9e.jpg",
                input_message_content=InputTextMessageContent(
                    message_text="""Here is the All Details of the BoT"""
                )
            )
        ],
        cache_time=0
    )

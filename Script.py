class script(object):
    START_TXT = """๐๐ {},

๐ญ๐๐ผ๐พ ๐๐ See ๐๐๐ Starting Me 
๐จ'๐ ๐บ ๐ฑ๐ฐ๐ธ๐ฆ๐ณ๐ง๐ถ๐ญ ๐๐ณ๐ฐ๐ถ๐ฑ ๐๐ข๐ข๐ฏ๐ข๐จ๐ฆ๐ณ ๐ธ๐ช๐ต๐ฉ ๐๐๐พ - ๐ฟ๐๐๐ผ๐๐๐๐๐พ๐ฝ ๐บ๐๐๐๐ฟ๐๐๐๐พ๐ ๐ป๐๐

๐๐ต๐ ๐พ๐บ๐๐ for ๐๐ ๐๐๐พ ๐๐พ; ๐๐๐๐ ๐๐ฝ๐ฝ ๐๐พ ๐๐ ๐ ๐๐๐ ๐๐๐๐๐ ๐บ๐ ๐๐ฝ๐๐๐, ๐๐๐ /help ๐ฟ๐๐ ๐๐๐๐พ ๐๐ฆ๐ข๐ต๐ถ๐ณ๐ฆ๐ฆ๐ด:
โโโโโโโโโโโโโ
ยฉMแดษชษดแดแดษชษดแดD Bส : <a href='tg://user?id=2107036689'><b>Naveen-TG,๐ฎ๐ณ [OfFLiNe],</b></a> .</b>"""

    HELP_TXT = """<b>๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐</b>: 
/start - ๐ผ๐๐พ๐ผ๐ ๐๐๐พ๐๐๐พ๐ ๐๐ ๐๐๐๐๐๐พ 
/help - ๐๐พ๐ ๐๐๐๐ ๐๐พ๐๐ ๐๐พ๐๐๐บ๐๐พ
/about - ๐บ๐ป๐๐๐ ๐๐พ"""
    
    ABOUT_TXT = """<b>โฅ ๐๐ฎ ๐๐๐ข๐ : <a href='https://t.me/VijayFilterTG_Bot'>๐๐๐๐ก๐๐ฅ๐๐ฉ๐๐ฎ ๐๐๐๐๐ฎ</a>

โฅ ๐พ๐ง๐๐๐ฉ๐ค๐ง : <a href='https://t.me/Dhanush_TG'>Dhanush-TG</a>

โฅ ๐๐๐๐ง๐๐ง๐ฎ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>

โฅ ๐๐๐ฃ๐๐ช๐๐๐ : Python ๐น

โฅ ๐ฟ๐๐ฉ๐ ๐ฝ๐๐จ๐ : <a href='https://www.mongodb.com/'>MongoDB</a>

โฅ ๐ฝ๐ค๐ฉ ๐๐๐ง๐ซ๐๐ง : <a href='https://heroku.com'>Heroku</a>

โฅ ๐ฝ๐ช๐๐ก๐ ๐๐ฉ๐๐ฉ๐ช๐จ : v2.0.1 [ Beta ]"""

    WIKIPEDIA_TXT = """Help: <b>Wikipedia</b>

<b>Commands and Usage:</b>

- Use /wiki < Query > To Get the Information about the query"""

    ABOUTME_TXT = """<b>โฅ ๐๐ฎ ๐๐๐ข๐ :  <a href='https://t.me/VijayFilterTG_Bot'>๐๐๐๐ก๐๐ฅ๐๐ฉ๐๐ฎ ๐๐๐๐๐ฎ</a>

โฅ ๐พ๐ง๐๐๐ฉ๐ค๐ง : <a href='https://t.me/Dhanush_TG'>Dhanush-TG</a>

โฅ ๐๐๐๐ง๐๐ง๐ฎ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>

โฅ ๐๐๐ฃ๐๐ช๐๐๐ : Python ๐น

โฅ ๐ฟ๐๐ฉ๐ ๐ฝ๐๐จ๐ : <a href='https://www.mongodb.com/'>MongoDB</a>

โฅ ๐ฝ๐ค๐ฉ ๐๐๐ง๐ซ๐๐ง : <a href='https://heroku.com'>Heroku</a>

โฅ ๐ฝ๐ช๐๐ก๐ ๐๐ฉ๐๐ฉ๐ช๐จ : v2.0.1 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>

Thalapathy Vijay is not a Open source project.

๐ฒ๐ฎ๐ด๐ฑ๐ข๐ค ๐ข๐ฎ๐ฃ๐ค ~ ๐ญ๐ฎ๐ณ ๐ ๐ต๐ ๐จ๐ซ๐ ๐ก๐ซ๐ค ๐ฑ๐จ๐ฆ๐ง๐ณ ๐ญ๐ฎ๐ถ</b>

<b>๐ฎ๐ณ๐ง๐ค๐ฑ ๐ช๐จ๐ญ๐ฃ ๐ก๐ฎ๐ณ๐ฒ:</b>

<b>๐ ๐ด๐ณ๐ฎ ๐ฅ๐จ๐ซ๐ณ๐ค๐ฑ</b> : <a href='https://github.com/EvamariaTG/EvaMaria'>๐ค๐๐บ ๐ฌ๐บ๐๐๐บ</a>
<b>๐ฒ๐ฎ๐ญ๐ฆ</b> :  <a href='https://github.com/AsmSafone/RadioPlayerV2'>๐ ๐๐๐ฒ๐บ๐ฟ๐๐๐พ</a>
<b>๐ฅ๐จ๐ซ๐ณ๐ค๐ฑ</b> : <a href='https://github.com/TroJanzHEX/Unlimited-Filter-Bot'>๐ด๐๐๐๐๐๐๐พ๐ฝ ๐ฅ๐๐๐๐พ๐ ๐ก๐๐</a>
<b>PLUGINS</b> : <a href='https://github.com/ctzfamily/waifuFunBot'>WaifuFunBot</a>

<b>Onwer:</b>
- <a href='https://t.me/Naveen_TG'>Naveen-TG</a>

<b>Devs:</b>

- <a href='https://t.me/rsrmusic'>๐๐๐</a>
- <a href='https://t.me/NandhaxD'>ใใณใ โฐ ยป โธ๏ธโ๏ธ ยซ โฎ</a>
- <a href='https://t.me/Masterolic'>โ๏ธปใEฬทtฬทhฬทiฬทcฬทaฬทlฬท ฬท Hฬทaฬทcฬทkฬทeฬทrฬทโโโไธ</a>
- <a href='https://t.me/Abhisheksvlog'>เผแถสณแตแถปสธแดฎแดผหขหขๅไนๅไธจไธๅไนาเผ</a>


"""

    SHAZAM_TXT = """<b>Shazam Music Founder Module</b>

<b>Usages</b>

- Helps You To Recognize | Discover a Song

<b>Commands</b>

- Send /Shazam (Reply To A Song File)

<b>Problems</b>

-If The feature is not working in your bot pls contact him :<a href='tg://user?id=1951205538'><b>Click Here</b></a>

<b> What's The Use </b>

- Do You Want To Know A Song Name So You Can Hear It 
Don't Worry Send /shazam"""

    IP_TXT = """<b>IP Address Finder Module</b>

- if you want to Find Details of a IP Address Use the Module

<b>Command</b>

- /ip [Ip address]
- ex /ip 192.180.0.1"""

    LYRICS_TXT = """<b>Lyrics ๐ฃ๐๐๐๐๐๐บ๐ฝ ๐ฌ๐๐ฝ๐๐๐พ</b>

- ๐จ๐ฟ ๐๐๐ ๐๐บ๐๐ ๐๐ ๐ฝ๐๐๐๐๐๐บ๐ฝ ๐บ lyric, ๐ฝ๐๐'๐ ๐๐พ๐บ๐๐ผ๐ ๐ฟ๐๐ ๐๐๐๐พ๐ ๐ป๐๐ ๐๐พ๐๐พ ๐๐ ๐๐๐พ ๐บ๐๐ ๐๐ ๐๐๐พ ๐ป๐๐

<b>๐ข๐๐๐๐บ๐๐ฝ</b>

- /lyrics [Song Name] - ๐ณ๐ ๐๐พ๐ ๐๐๐พ lyrics

<b>Usage</b>

- ๐ข๐บ๐ ๐ป๐พ ๐๐๐พ๐ฝ ๐ป๐ ๐พ๐๐พ๐๐ ๐๐๐พ
- ๐ถ๐๐๐๐ ๐๐๐๐ ๐๐ ๐ป๐๐๐ ๐๐

<b>๐ก๐๐</b>

๐ฒ๐๐๐พ๐๐๐๐พ๐ ๐๐ ๐๐๐๐ ๐๐๐๐ ๐บ๐ ๐พ๐๐๐๐!"""

    CARBON_TXT = """Reply To a Message To Make CarBon use /carbon for using this Module"""

    IMG_TXT = """If You Want To Make A image Of Text send
/hand <anything> to Get the Photo"""

    FONTS_TXT = """ Want Some Stylish fonts send /font <anything>"""

    BOTSTATUS_TXT = """Send /status for getting bot and heroku status"""

    MAMMOKA_TXT = """๐๐๐๐๐๐๐ : <b>Iแดแดแด Fแดษดs Aสแด Pสแดสษชสษชแดแดแด Nแดแดส Tสษชs แดสแดแด</b> 
    
    <b> ๐๐๐ผ๐๐๐: </b>
    Tสษชs าษชสแดแดส แดแดษดแดแดษชษดs แดแดxษชแด าแดษดษดส sแดษชแดแดแดสs ๐๐๐
    
    <b> ๐พ๐๐๐๐ผ๐๐ฟ: </b> /ikka โบโบ
    
    """

    ABOUTIME_TXT = """<b>โฅ ๐๐ฎ ๐๐๐ข๐ : {}

โฅ ๐พ๐ง๐๐๐ฉ๐ค๐ง : <a href='https://t.me/Y2say'>Dhanush-TG</a>

โฅ ๐๐๐๐ง๐๐ง๐ฎ : <a href='https://docs.pyrogram.org/'>Pyrogram</a>

โฅ ๐๐๐ฃ๐๐ช๐๐๐ : Python ๐น

โฅ ๐ฟ๐๐ฉ๐ ๐ฝ๐๐จ๐ : <a href='https://www.mongodb.com/'>MongoDB</a>

โฅ ๐ฝ๐ค๐ฉ ๐๐๐ง๐ซ๐๐ง : <a href='https://heroku.com'>Heroku</a>

โฅ ๐ฝ๐ช๐๐ก๐ ๐๐ฉ๐๐ฉ๐ช๐จ : v2.0.1 [ Beta ]
    
โค ๐ธ๐ ๐ข๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐ โค๏ธโก"""

    NEXT_TXT = """Welcome To My Second Help Module"""

    NEXTT_TXT = """Welcome To My Third Help Module"""

    WARN_TXT = """Here is the help for the <b>Warns</b> module:

Keep your members in check with warnings; stop them getting out of control!
If you're looking for automated warnings, read about the blacklist module!

<b>Admin Commands</b>:

- /warn <reason>: Warn a user.

- /dwarn <reason>: Warn a user by reply, and delete their message.

- /swarn <reason>: Silently warn a user, and delete your message.

- /warns: See a user's warnings.

- /rmwarn: Remove a user's latest warning.

- /resetwarn: Reset all of a user's warnings to 0.

- /resetallwarns: Delete all the warnings in a chat. All users return to 0 warns.

- /warnings: Get the chat's warning settings.

- /setwarnmode <ban/kick/mute>: Set the chat's warn mode.

- /setwarnlimit <number>: Set the number of warnings before users are punished.

<b>Examples</b>
- Warning a user.

-> /warn @user For disobeying the rules"""

    URL_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>

โข /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>

<code>/short https://t.me/TamilMV_Collections</code>

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>

<b>Commands and Usage</b>:

โข /torrent or /tor : Get Your Torrent Link From Various Resource.

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    DISABLE_TXT = """Here is the help for the <b>Disabling</b> module:

This allows you to disable some commonly used commands, so noone can use them. It'll also allow you to autodelete them, stopping people from bluetexting.

<b>Admin commands</b>:

ร /disable <commandname>: Stop users from using commandname in this group.
ร /enable <item name>: Allow users from using commandname in this group.
ร /disableable: List all disableable commands.
ร /disabledel <yes/no/on/off>: Delete disabled commands when used by non-admins.
ร /disabled: List the disabled commands in this chat.

<b>Note</b>:

When disabling a command, the command only gets disabled for non-admins. All admins can still use those commands.
Disabled commands are still accessible through the /connect feature. If you would be interested to see this disabled too, let me know in the support chat."""
    
    RULES_TXT = """Here is the help for the <b>Rules</b> module:

Every chat works with different rules; this module will help make those rules clearer!

<b>User commands</b>:

ร /rules: Check the current chat rules.

<b>Admin commands</b>:

ร /setrules <text>: Set the rules for this chat.

ร /privaterules <yes/no/on/off>: Enable/disable whether the rules should be sent in private.

ร /resetrules: Reset the chat rules to default.

ร /rulesbtn <custom text>: Sets the text of rules button.

ร /resetrulesbutton: Reset the text of rules button to default.

ร /resetrulesbtn: Same as above."""

    NOTES_TXT = """Here is the help for the <b>Notes</b> module:

Save data for future users with notes!
Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!
User commands:

- /get <notename>: Get a note.

- #notename: Same as /get.

<b>Admin commands</b>:

- /save <notename> <note text>: Save a new note called "word". Replying to a message will save that message. Even works on media!

- /clear <notename>: Delete the associated note.

- /notes: List all notes in the current chat.

- /saved: Same as /notes.

- /clearall: Delete ALL notes in a chat. This cannot be undone.

- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM."""
    
    PURGE_TXT = """Here is the help for the <b>Purges</b> module:

<b>Admin only</b>:

- /purge: deletes all messages between this and the replied to message.
- /del: deletes the message you replied to.

<b>Examples</b>:

- Delete all messages from the replied to message, until now.
-> /purge"""

    APPROVE_TXT = """Here is the help for the <b>Approvals</b> module:

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send

<b>User commands</b>:
ร /approval: Check a user's approval status in this chat.

<b>Admin Commands</b>:

ร /approve: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
ร /unapprove: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
ร /approved: List all approved users.

<b>Group Owner Commands</b>:

ร /unapproveall: Unapprove ALL users in a chat. This cannot be undone."""

    LOCK_TXT = """Here is the help for the <b>Locks</b> module:

<b>Admin only</b>:

ร /lock <permission>: Lock Chat permission.

ร /unlock <permission>: Unlock Chat permission.

ร /locks: View Chat permission.

ร /locktypes: Check available lock types!

Locks can be used to restrict a group's users.
Locking urls will auto-delete all messages with urls, locking stickers will delete all stickers, etc.
Locking bots will stop non-admins from adding bots to the chat.

Example:

/lock media: this locks all the media messages in the chat."""
    FILE_TXT = """โค ๐๐๐ฅ๐ฉ: ๐๐ข๐ฅ๐ ๐๐ญ๐จ๐ซ๐ ๐๐จ๐๐ฎ๐ฅ๐../

<b>By Using This Module You can store files in My database and I will You A Permanent link To access The saved Files.If You want to add files from a Public channel send the file link only or You want to store files from a Private channel you must make me admin on their to access files files.../</b>

โชผ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐ โบ

โช /plink โบโบ <b>๐ฑ๐พ๐๐๐ ๐๐ ๐บ๐๐ ๐๐พ๐ฝ๐๐บ ๐๐ ๐๐พ๐ ๐๐๐๐.</b>
โช /pbatch โบโบ <b>๐ด๐๐พ ๐๐๐๐ ๐e๐ฝ๐๐บ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ.</b>
โช /batch โบโบ <b>To Create Link For Multiple Post.</b>

โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ

<code>/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336</code>"""

    WELCOME_TXT ="""Here is the help for the <b>Greetings</b> module:

Welcome new members to your groups or say Goodbye after they leave!

<b>Admin Commands</b>:

ร /setwelcome <reply/text>: Sets welcome text for group.

ร /welcome <yes/no/on/off>: Enables or Disables welcome setting for group.

ร /resetwelcome: Resets the welcome message to default.

ร /setgoodbye <reply/text>: Sets goodbye text for group.

ร /goodbye <yes/no/on/off>: Enables or Disables goodbye setting for group.

ร /resetgoodbye: Resets the goodbye message to default.

ร /cleanservice <yes/no/on/off>: Delete all service messages such as 'x joined the group' notification.

ร /cleanwelcome <yes/no/on/off>: Delete the old welcome message, whenever a new member joins."""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>

Note:- Give a user details

โข/whois :-give a user full details"""

    FUN_TXT ="""<b>Gแดแดแดs</b> 
    
<b>๐ฒ NOTHING MUCH JUST SOME FUN THINGS</b>

t๐๐ ๐๐๐๐ ๐ฎ๐๐: 

๐ฃ. /dice - Roll The Dice 
๐ค. /Throw ๐๐ /Dart - ๐ณ๐ ๐ฌ๐บ๐๐พ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""

    ENGLISH_TXT = """HELP:English
 โ /define <text>*:* Tสแดแด แดสแด แดกแดสแด แดส แดxแดสแดssษชแดษด สแดแด แดกแดษดแด แดแด sแดแดสแดส\ษดFแดส แดxแดแดแดสแด /define แดษชสส
 โ /spell*:* แดกสษชสแด สแดแดสสษชษดษข แดแด แด แดแดssแดษขแด, แดกษชสส สแดแดสส แดกษชแดส แด ษขสแดแดแดแดส แดแดสสแดแดแดแดแด แด แดสsษชแดษด
 โ /synonyms <word>*:* Fษชษดแด แดสแด sสษดแดษดสแดs แดา แด แดกแดสแด
 โ /antonyms <word>*:* Fษชษดแด แดสแด แดษดแดแดษดสแดs แดา แด แดกแดสแด
"""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>
a bot to create a link to share text in the telegram.
<b>Commands and Usage:</b>
โข /share (text or reply to message)
<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and แฉแแฉแญ  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. แฉแแฉแญ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    SONG_TXT = """<b>๐ผSong Download๐ผ</b>

Song Download Module, For Those Who Love Music

<b>๐ Command ๐</b>

- /song [Song Name] - To Download Music ๐

<b>๐Usage๐</b>

- Can Be Used By Everyone
- Works in bot pm

Made By <a href=https://t.me/+vAX64oYJuWU1NjE1>๐๐ ๐๐ฉ๐๐๐ญ๐๐ฌ</a>"""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>

โข /share (text or reply to message)

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
   
    PIN_TXT ="""<b>PIN MODULE</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>๐ Commands & Usage:</b>

โ /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
โ /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

โข /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS ๐ค module:</b>

Translate text to speech

<b>Commands and Usage:</b>

โข /tts <text> : convert text to speech

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>๐ Ping:</b>

Helps you to know your ping ๐ถ๐ผโโ๏ธ

<b>Commands:</b>

โข /alive - To check you are alive.
โข /help - To get help 
โข /ping - To get your ping 
โข /repo - Source Code. 

<b>๐นUsage๐น :</b>

โข This commands can be used in pms and groups
โข This commands can be used buy everyone in the groups and bots pm
โข Share us for more features"""
    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

๐คง /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>๐ฃPurge๐ฃ</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

โ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-แฉแแฉแญ  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. แฉแแฉแญ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+veUIdIW2CQ5mOGU5)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of แฉแแฉแญ 

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban_user  - <code>to ban a user.</code>
โข /unban_user  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>โช <b>Total Files:</b> <code>{}</code>
โช <b>Total Users:</b> <code>{}</code>
โช <b>Total Chats:</b> <code>{}</code>
โช <b>Used Storage:</b> <code>{}</code> 
โช <b>Free Storage:</b> <code>{}</code> """

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
   
    BOYCOTT_TXT = """help: Boycott
This command helps to Creates Boycott Image!

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

Use /boycott ( reply to a image for using boycott )

It Will Helps You To Kidd Your Friend 'X' 
Refered codes from FridayUB."""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    REPORT_TXT = """โค ๐๐๐ฅ๐ฉ: Rแดแดแดสแด โ ๏ธ

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐ ๐ ๐๐๐๐๐๐๐ ๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐. ๐ณ๐๐'๐ ๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐.

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/report ๐๐ @admins - ๐ณ๐ ๐๐พ๐๐๐๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐บ๐ฝ๐๐๐๐ (๐๐พ๐๐๐ ๐๐ ๐บ ๐๐พ๐๐๐บ๐๐พ)."""

    REPO_TXT = """help Git Repo Finder Module.

Use /repo { Repo name } to Get a Repo of GitHub

Example : /repo Eva Maria."""

    CORONA_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ข๐๐๐๐ฝ

๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐  ๐๐๐๐๐ข ๐๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
/covid ๐จ๐๐ฝ๐๐บ"""

    URLSHORT_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ด๐๐ ๐๐๐๐๐๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐ ๐ ๐๐๐ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /short: ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐พ๐ ๐๐๐๐๐๐พ๐ฝ ๐๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
/short https://t.me/+veUIdIW2CQ5mOGU5"""

    IFSC_TXT ="""Help to Get ifsc Code Info."""

    VIDEO_TXT ="""๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐๐ธ๐ณ๐ด๐พ ๐ต๐๐พ๐ผ ๐๐พ๐๐๐๐ฑ๐ด.

โข ๐๐ด๐ข๐จ๐ฆ
๐ ๐ฐ๐ถ ๐๐ข๐ฏ ๐๐ฐ๐ธ๐ฏ๐ญ๐ฐ๐ข๐ฅ ๐๐ฏ๐บ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ณ๐ฐ๐ฎ ๐ ๐ฐ๐ถ๐ต๐ถ๐ฃ๐ฆ

๐๐ค๐ฌ ๐๐ค ๐๐จ๐
โข ๐๐บ๐ฑ๐ฆ /video or /mp4 ๐๐ฏ๐ฅ (๐๐ช๐ฅ๐ฆ๐ฐ Link)
โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ:
/๐ฎ๐ฑ4 https://youtu.be/Your Link"""

    COUNTRY_TXT = """โค ๐๐๐ฅ๐ฉ: Country

Just use /country ( Country Name ) for knowing the country info."""

    ZOMBIES_TXT = """๐ท๐ด๐ป๐ฟ ๐๐พ๐ ๐๐พ ๐บ๐ธ๐ฒ๐บ ๐๐๐ด๐๐

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """โค ๐๐๐ฅ๐ฉ: Iแดแดษขแด

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ข ๐๐๐๐๐๐ข 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช ๐ฉ๐๐๐ ๐๐พ๐๐ฝ ๐๐พ ๐บ ๐๐๐บ๐๐พ ๐๐ ๐พ๐ฝ๐๐ โจ

๐ฌ๐บ๐ฝ๐พ ๐ป๐ <a href=https://t.me/+veUIdIW2CQ5mOGU5>๐๐ ๐๐ฉ๐๐๐ญ๐๐ฌ</a>"""

    STICKER_TXT = """๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ธ๐ ๐ผ๐พ๐ณ๐๐ป๐ด ๐๐พ ๐ต๐ธ๐ฝ๐ณ ๐ฐ๐ฝ๐ ๐๐๐ธ๐ฒ๐บ๐ด๐๐ ๐ธ๐ณ.
โข ๐๐๐๐๐
To Get Sticker ID
 
  โญ ๐๐ค๐ฌ ๐๐ค ๐๐จ๐
 
โ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """๐ท๐ด๐ป๐ฟ๐ ๐๐พ ๐ณ๐พ๐๐ฝ๐ป๐พ๐ฐ๐ณ ๐ฐ๐ฝ๐ ๐๐พ๐๐๐๐ฑ๐ด ๐๐ธ๐ณ๐ด๐พ ๐๐ท๐๐ผ๐ฑ๐ฝ๐ฐ๐ธ๐ป
    
โญ๐๐ค๐ฌ ๐๐ค ๐๐จ๐
๐๐บ๐ฑ๐ฆ /ytthumb ๐๐ฏ๐ฅ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ช๐ฏ๐ฌ

โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ
/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ ๐๐ฝ๐๐๐ป๐๐๐

๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐ฟ๐ณ๐ต ๐๐๐๐ ๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /audiobook: ๐ฑ๐พ๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐ ๐บ๐๐ ๐ฏ๐ฃ๐ฅ ๐๐ ๐๐พ๐๐พ๐๐บ๐๐พ ๐๐๐พ ๐บ๐๐ฝ๐๐"""

    GTRANS_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ฆ๐๐๐๐๐พ ๐ณ๐๐บ๐๐๐๐บ๐๐พ๐

๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐ข๐๐ ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ ๐๐๐ก๐ ๐๐ ๐บ๐๐ ๐๐๐๐๐๐๐๐๐ ๐ข๐๐ ๐ ๐๐๐. ๐๐๐๐ ๐๐๐๐๐๐๐ ๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐ โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/tr - ๐ณ๐ ๐๐๐บ๐๐๐๐บ๐๐พ๐ ๐๐พ๐๐๐ ๐๐ ๐บ ๐๐๐พ๐ผ๐๐ฟ๐ผ ๐๐บ๐๐๐๐บ๐๐พ

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tr ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐บ๐๐๐๐บ๐๐พ ๐ผ๐๐ฝ๐พ

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ ๐๐
โข ๐พ๐ = ๐ค๐๐๐๐๐๐
โข ๐๐ = ๐ฌ๐บ๐๐บ๐๐บ๐๐บ๐
โข ๐๐ = ๐ง๐๐๐ฝ๐"""

    RESTRIC_TXT = """โค ๐๐๐ฅ๐ฉ: Mแดแดแด ๐ซ

๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐ ๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐๐ข.

โช/ban: ๐ณ๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐ฟ๐๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unban: ๐ณ๐ ๐๐๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tban: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐.
โช/mute: ๐ณ๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unmute: ๐ณ๐ ๐๐๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tmute: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐.

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tmute ๐๐ /tban ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐๐๐พ ๐๐๐๐๐.

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ป๐บ๐ 2๐ฝ ๐๐ /๐๐๐๐๐พ 2๐ฝ.
๐ธ๐๐ ๐ผ๐บ๐ ๐๐๐พ ๐๐บ๐๐๐พ๐: ๐/๐/๐ฝ. 
 โข ๐ = ๐๐๐๐๐๐พ๐
 โข ๐ = ๐๐๐๐๐
 โข ๐ฝ = ๐ฝ๐บ๐๐"""
    CREATOR_REQUIRED = """โ<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """๐ฎ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """โ<b>เดเดจเตเดจเต Admin เดเดเตเดเดคเตเดค เดธเตเดฅเดฒเดคเตเดคเต เดเดพเตป เดจเดฟเดเตเดเดฟเดฒเตเดฒ เดชเตเดเตเดตเดพ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>เดเดชเตเดชเต เดเดฒเตเดฒเดพเด เดเดเดฟเดเตเดเตเดฎเดพเดฑเตเดฑเดฟ เดคเดฐเดพเด...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""




# Poems Generated from 1000 Most Common English Phrases
See it at [https://poetry.aqring.com]
## Origin
This is a flask web app that generates something, and depending on how loose your definition of 'poetry' is, it may indeed generate 'poetry'.

This app started as a weird google hole I used to climb in for fun where I would google 'How to learn English', but translated into other languages to see what language learning material looked like if you only knew the language being taught and not the language it was being taught *in*.

Eventually I came across a website which claimed to have the '1000 most common English phrases' and included their Chinese translation. After looking at the phrases I decided quickly that they were not the most common phrases by any stretch of the imagination and indeed some of them have probably never been spoken in English conversation at all. 

> 408.	I smelled a smell of cooking.	我聞到了燒菜做飯的味道。

> 654.	He is commonly supposed to be foolish.	他是公認的傻瓜。

> 875.	How can I climb up that wall! I wish I were a bird!	我怎麼能夠爬得上那堵牆?我要是一隻鳥就好了!

Some of the phrases were pretty boring factual stuff.
> 881.	Most of the earth's surface is covered by water.	大部分的地球表面被水覆蓋著。

> 469.	The eggs are sold by the dozen.	雞蛋按打賣。

But, some of them were interesting.

> 465.	My false teeth are stuck to it.	我的假牙還在上邊呢!

> 189.	Love me, love my dog.	(諺語)愛屋及烏。

> 829.	This is by far the largest cake in the world.	這是目前世界上最大的蛋糕了。

I got the notion that if you picked any random four of these phrases, you might get something unintentionally poetic, funny or at least entertaining enough to make us forget about the horror of existence for the briefest moment.

For example:

> 
    How ever you may work hard, the boss will not be fully satisfied.

    He drives more carefully than you.

    He owes my uncle $100

    The brain needs a continuous supply of blood.

>
    He had to choose between death and dishonor.

    I can't help eating sweets whenever they are in my presence.

    The price just covers the cost.

    After a pause he continued his story.

## Notes

The phrases are stored in an sqlite database. The front page uses [htmx](https://htmx.org) for infinite scrolling. 

Each poem is framed with a random color.

The /poem route can decode a specific poem allowing permalinks.









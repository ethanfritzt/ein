# Ein

A discord bot for me and my friends. _BORF!_

# Contribution Guides

## Fork and clone

1. First you want to Fork this repository. The fork button can be found in the upper right hand corner of your webpage. This makes a _copy_ of this repository for yourself.

![](/img/ForkScreenCap.png)

2. Second you'll want to clone your forked repository, so head over to your forked repository and hit the `Code` button.

![](/img/CloneScreenCap.png)

- Either use `https` or `ssh`. `ssh` is recomended, but setting up ssh keys can be a hassle. Here is a great link to ssh keys: https://docs.gitlab.com/ee/user/ssh.html

3. Create a a discord application. You can create an application here: https://discord.com/developers/applications

- You'll want to create a new application by clicking the new application button in the upper right hand corner. Follow the steps to get an access token.

- With the newly aquired access token. Go into your cloned repositiory on your machine. Create a `.env` file, simply just named `.env` and add this `TOKEN=<your access token>`.

4. Finally, invite your bot to a server. You can do this by clicking on `OAUTH2` in your applications dashboard on the discord developer site, clikc on `URL GENERATOR` and then inside of that check the box labeled `bot` a new set of checkboxes should appear, then click `Administrator`. Copy the link and paste it into your web browser and then select a server.

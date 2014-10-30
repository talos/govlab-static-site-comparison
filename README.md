## GovLab Static Python Static Site Generator Smackkdown

In the red corner: [Pelican][http://blog.getpelican.com/]

In the blue corner: [Nikola][http://www.getnikola.com]

Here's a list of their shared attractive attributes, which is why they were put
in competition:

* Posts can be written in Markdown
* Templates and pages can be edited in Jinja2
* Tags are supported
* Written in Python
* Supports easy deploy to GitHub.
* Actively being developed by numerous developers, FOSS to boot

So... the comparison!

### Installation

Both support an easy install process using `pip install`, but default to
ReStructured Text, so Markdown has to be installed separately.

So for Pelican:

`pip install pelican markdown`

Make sure to enter `y` when asked `> Do you want to upload your website using
GitHub Pages? (y/N)`, as it defaults to `N`.

And Nikola:

`pip install nikola markdown`

Of course, this working depends on a functional Python/distribute environment
on the client's computer, which can be a headache.  Also, `virtualenv` is
recommended so you don't pollute your system Python.  But those are more
criticisms of Python and its ecosystem than these site generators -- and it's
not like the situation is any better in Rubyland (`rvm`, anyone?)

__Victor__: everybody wins!  But Pelican does a little bit more, since [their
docs] mention installing markdown from the start.

  [their docs]: http://docs.getpelican.com/en/3.4.0/quickstart.html#installation

### Generating a site skeleton

Both have tools to generate a barebones site to work from quickly.  Pelican has
a special-purpose commandline tool for this:

`pelican-quickstart`

While Nikola has a single command line tool, which supervises numerous commands
including site generation:

`nikola init`

Both tools allow you to specify a target directory, and ask a series of basic
questions (what's the name of the blog?  Who is the author?) to populate the
initial configuration.

Nikola's design is simpler and clearer here.  If you naïvely execute `pelican`
instead of `pelican-quickstart`, Pelican will assume you want to regenerate
your current folder and create a bunch of junk (whether or not there's
a pelican project there.  Its error messages don't suggest you need to run
`pelican-quickstart`; you have to look at docs online to find that out.

```
$ pelican
WARNING: Feeds generated without SITEURL set properly may not be valid
WARNING: No timezone information specified in the settings. Assuming your
timezone is UTC for feed generation. Check
http://docs.getpelican.com/en/latest/settings.html#timezone for more
information
ERROR: Skipping posts/data-ruled-irrelevant.rst: could not find information
about 'date'
Done: Processed 0 article(s), 0 draft(s) and 0 page(s) in 0.19 seconds.
```

With Nikola, simply executing `nikola` will give you a helpful listing of the
possible commands, including the relevant `init` command:

```
$ nikola
[2014-10-29T21:13:38Z] WARNING: Nikola: In order to USE_BUNDLES, you must
install the "webassets" Python package.
[2014-10-29T21:13:38Z] WARNING: Nikola: Setting USE_BUNDLES to False.
Nikola is a tool to create static websites and blogs. For full documentation
and more information, please visit http://getnikola.com/


Available commands:
  nikola auto                 automatically detect site changes, rebuild and
optionally refresh a browser
  nikola bootswatch_theme     given a swatch name from bootswatch.com and
a parent theme, creates a custom theme
  nikola build                run tasks
...
```

__Victor__: Nikola, for elegance.

### Creating your first blog post

All new posts follow roughly the same format in Pelican.  According to the
[quickstart guide][] this means duplicating a template post of this format:

  [quickstart guide]: http://docs.getpelican.com/en/3.4.0/quickstart.html#installation

```
Title: (title)
Date: (date)
Category: (list of categories)

(Content goes here.)
```

And placing it, with a `.md` extension (if you're using Markdown,) in the
pregenerated `content` folder.  If you do this yourself, make sure to write the
date the way Pelican expects!  If you write, say `10/11/2012 10:20` or
`2012/10/11 10:20` instead of `2012-10-11 10:20`, Pelican will complain with
the almost-helpful:

`ERROR: Skipping ./blogpost.md: could not find information about 'date'`

It would be nice if it specified how to properly write a date -- otherwise
you'll probably find yourself referring to prior posts or the documentation.

It's also worth noting that if you forget to install `markdown` via pip when
you install Pelican, it will simply mysteriously ignore your Markdown posts.
Annoying!

Nikola's CLI provides a utility for creating new posts.

`nikola new_post`

This will prompt you for title, etc.  It auto-generates the date, which is
actually quite convenient.

On the other hand, it assumes you want to use ReStructured Text, and you will
need to use a special switch to use Markdown instead.  Unfortunately, the naive

`nikola new_post -f markdown` will spit out the error message:

```
Exception: Can't find a way, using your configuration, to create a post in format markdown. You may want to tweak COMPILERS or POSTS in conf.py
```

The trick is to edit `conf.py` to insert a line translating `.md` formats for
both `POSTS` and `PAGES`:

```
POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.rst", "stories", "story.tmpl"),
    ("stories/*.txt", "stories", "story.tmpl"),
    ("stories/*.md", "stories", "story.tmpl"),
)
```

It would've been nice if this was in the config, perhaps commented out since
markdown isn't bundled in the package.

PS: Make sure you installed the Markdown module via `pip`!  If you didn't, you
still can:

`pip install markdown`

_Victor_: Nikola, since it provides a nice utility that auto-generates your
dates.  Really, this is surprisingly annoying to do manually.  While I wasn't
a fan of the extra setup to get Nikola recognizing Markdown, at least it goes
out of its way to complain when it doesn't recognize content in your content
folder -- I really don't like it when something fails silently!

## Generating the blog

Static sites need to be "generated", or transformed from the source Markdown
and Jinja2 templates in their own folders to a folder of HTML output in the
same organization as the URL scheme of your site.

In Pelican, this is done through the `pelican` command:

`pelican`

By default, this will look for articles in the folder called `content`
(generated by `pelican-quickstart`).  Output goes in the `output` folder,
which can be customized with the `-o` flag.  Additional flags allow you to
customize the theme and location of the configuration file.

Nikola has a similar `build` command:

`nikola build`

This doesn't appear to let you customize the location of input and output, but
if you're using the skeleton setup Nikola provides, this shouldn't be a big
deal.  It also lets you run the build in several processes, and won't re-run it
if nothing has changed since the last run.

__Victor__: Kind of a tossup.  Nothing decisively superior about either.

### Previewing your blog locally

Static sites are super-easy to preview, since the server doesn't have to
execute any site-specific code or connect to a database.

Pelican takes advantage of this simplicity and tells its users to utilize
Python's built in `SimpleHTTPServer`:

`python -m SimpleHTTPServer`

However, by default `pelican-quickstart` also creates a Makefile, that can be
used for convenience:

`make serve`

Nikola makes things a little easier to remember by building that into its CLI,
although it [maps to something similar][]:

  [maps to something similar]: https://github.com/getnikola/nikola/blob/62fa7db704d8a4f5a5046668b4211dfd1eb231b8/nikola/plugins/command/serve.py#L84

`nikola serve`

This allows for a little extra documentation (if you look at `nikola serve -h`)
about features like switching the port, in case you've got a different service already running on 8000.

__Victor__: Nikola, for superior documentation.

### Deploying to a GitHub as a remote

GitHub pages is a cheap, reliable way to host a static site.

For Pelican GH Pages was one of the options for deploying offered at the end of
`pelican-quickstart`.  Hopefully you said `y` then!

If you naïvely try

`make github`

you'll get a helpful error:

`make: ghp-import: No such file or directory`

Indeed, we need `ghp-import`, which is a very useful tool that can be installed
from pip:

`pip install ghp-import`

After installing `ghp-import`, `make github` works great.

Nikola has a builtin command for deploying to github, `nikola github_deploy`.
Unfortunately, it has a serious [bug][] at the moment, and won't work unless
you've already created a blank `gh-pages` branch and pushed it to GitHub.

  [a bug]: https://github.com/getnikola/nikola/issues/1464

This means you have to do this yourself, which can be dangerous -- make sure
you've committed everything on `master` and no untracked files are hanging out
before doing this!

```
git checkout --orphan gh-pages
git rm -rf .
git checkout master
```

__Victor__:

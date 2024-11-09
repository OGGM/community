# {octicon}`dependabot` Administrating the OGGM hubs

This guide is for teachers and admins of the hub(s). Please read it carefully if you are using the hubs for a class.

- https://hub.oggm.org
- https://classroom.oggm.org

## Soft & hardware

Both hub and classroom are running "The Littlest JupyterHub" ([TLJH](https://tljh.jupyter.org/en/latest/)), designed for local deployment rather than on the cloud. It does not use Kubernetes to scale resources based on user load. Instead, it utilizes the available machine resources without scaling.

OGGM Classroom is essentially a "clone" of OGGM Hub. They run the same version of TLJH, so they are nearly identical, but they maintain completely separate internal databases of users and environments.

Both the classroom and the hub operate on the same virtual machine in Bremen.

## Resources and storage

The virtual machine hosting the hubs is allocated with **8 CPUs and up to 96GB of RAM. All logged-in users on both the hub and classroom share these resources.**

Each user is allocated 10GB of disk space. This storage is “permanent” until an admin deletes the user account. Over several years, we have never lost data, which is quite remarkable (thanks to Timo). **However, we do not guarantee the safety of user data and encourage regular data backups.**

## Classroom or Hub?

Classroom allocates fewer resources per user (2 CPUs and 2GB each) compared to the hub (4 CPUs and 8GB). It’s unclear how these numbers impact performance, as users seem able to use more RAM than allocated.

Importantly, **we will delete users on Classroom eventually**. This is because students typically do not return after their class ends. We plan to delete all users during the summer break or shortly thereafter, identifying them by their class & year prefix.

## Monitoring resource usage during a class

Timo and I can access a dashboard to monitor CPU and RAM usage. We can assist with this monitoring during your class sessions.

## Environments and python packages

Upon logging in, users select from various “environments,” which are Docker images. Admins have control over these environments: building them is typically labor-intensive, and currently, Fabien builds them using Timo’s [repo2docker scripts](https://github.com/OGGM/r2d). These images include OGGM and most scientific packages.

Users can install packages via pip or conda during their sessions, but this is intended only for urgent fixes. Installed packages do not persist between sessions.

**If you need a specific package, please inform us well in advance so we can prepare a new environment.**

## User disk space, `home` and `shared` folder

Each user is assigned 10GB of space. When a user logs in, the hub launches a Python server for them and “mounts” this 10GB disk to their `home`.

All users are called `jovyan`, and their data resides in `/home/jovyan`. Users should not write outside of this directory and if they do, it'll be likely overwritten at next login.

A shared folder is available at `/home/jovyan/shared`. Users can read from and write to this folder. We advise students **to not write in `shared` directly**. Instead, they should copy data/scripts to their home directory before making changes.

## User management

User management is a bit of a pain at the moment.

Admins have the capability to add and delete users and change their passwords. This can be done through the hub control panel or via direct URLs:

- https://classroom.oggm.org/hub/admin#/ allows you to spawn or access a user’s server (evil but sometimes necessary), and delete users.
- https://classroom.oggm.org/hub/authorize manages passwords and user activation.

**To get an account**, users need to register themselves at https://classroom.oggm.org/hub/signup. They choose a username and a password, and then admins can "authorize" them. Admins do not receive a notification when a user wants to create an account (this is silly I know), so we have to check the authorize page regularly.

Admins can adminstrate user creation in two ways:
1. they send the signup link to students and they have to register themselves. Admins have then to authorize them before class. This is less labor intensive for admins.
2. admins register the students themselves and create a username / password for each of them, authorize them, and send the username / password to the students. This is easier for the students since they are given credentials and an account ready to use.

When administering user accounts, **please ensure that users adhere to the agreed format for usernames**.

**On classroom**, use a university prefix and a year (e.g., uob24_) followed by the student’s ID or name. This helps prevent user overlap and allows safe deletion of user groups after class completion. Please let us know your chosen prefix and add it to the wiki for transparency.

As an admin, ensuring compliance with this naming convention simplifies everyone’s job.

You can delete a user from the admin panel by clicking on the user and selecting delete.

## Accessing the tutorials (and other content) with nbgitpuller

By default, user space after logging in should be empty (except for the shared folder). We recommend teaching your students to use [nbgitpuller](https://jupyterhub.github.io/nbgitpuller) to automatically download content from any repository.

For example, to download from the [OGGM tutorials repository](https://github.com/OGGM/tutorials), execute this command in a JupyterHub terminal (`Launcher -> Start a terminal`):

```bash
gitpuller https://github.com/OGGM/tutorials master tutorials
```

This command will copy the notebooks into the `tutorials` folder in the home directory on the hub. You can use a similar command to pull content from other repositories as well, such as the [OGGM-Edu notebooks](https://github.com/OGGM/oggm-edu-notebooks).

Another way to pull content into your hub is by using a special weblink. the [nbgitpuller link generator](https://jupyterhub.github.io/nbgitpuller/link)  creates links that, once clicked, will open your workspace with the new notebooks. Here are some useful links to add notebooks to your hub:

- [Add OGGM's tutorial notebooks to classroom](https://classroom.oggm.org/hub/user-redirect/git-pull?repo=https%3A//github.com/OGGM/tutorials&urlpath=lab/tree/tutorials/./notebooks/welcome.ipynb&branch=stable)
- [Add OGGM-Edu notebooks to classroom](https://classroom.oggm.org/hub/user-redirect/git-pull?repo=https%3A//github.com/OGGM/oggm-edu-notebooks&urlpath=lab/tree/oggm-edu-notebooks/./welcome.ipynb&branch=master)

**Important:**

nbgitpuller will never overwrite changes that **the user** has made to the files in the pulled folder. This is crucial to remember: sometimes you might want your students to get an updated version of the notebooks, for example, and this will not work if they have made changes to those files. Therefore, it is always a good idea to make a working copy of the original file/folder before working on it (right-click -> rename).

The full set of rules used by nbgitpuller while pulling is explained [here](https://jupyterhub.github.io/nbgitpuller/topic/automatic-merging.html).

## Privacy notice

Visit and read the [[Hub Privacy Notice]] and remind your students that this exists.

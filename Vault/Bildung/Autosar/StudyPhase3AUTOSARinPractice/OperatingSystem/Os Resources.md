An Os Resource can be used to protect against concurrent access by at least two concurrent tasks without using Interrupt locks. They are also using Priority Ceiling Protocol.

Below you can see an example of a shared resource between tasks and how it is protected.

Because Task A accesses the resource with GetResource the Task B cannot access the resource.

Here the Task A no longer blocks the resource because of the ReleaseResource. Task B can access the resource with GetResource.
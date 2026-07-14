# W0D0 Behavioral Readout - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial3.html
- YouTube: https://youtube.com/watch?v=1DsxzkaLTOQ
- Caption track: en (manual)

## 01 · 00:00:00.480 - 00:00:36.960

Hi I am Ella Betty and I'm going to be talking about behavioral readouts in typical neuroscience experiments. So let's start with why we want to read behavior? We often just care about behavior itself, so just by studying the behavior of animals we can start to understand the strategies they use behind decision making, the types of memories they form, and the qualities of those memories, and how they perceive sensory information among many other things. As neuroscientists though we often also want to relate behavior to

## 02 · 00:00:36.960 - 00:00:54.640

neural activity. So typically when we're recording from the brain of an animal we want to relate it to something the animal is experiencing or doing. So in some experiments, we'll just have the animal be pretty passive and will show sensory stimuli to that animal like a video.

## 03 · 00:00:56.160 - 00:01:12.880

In these cases, we probably don't care as much about the animal behavior because it's not really doing anything it's just taking in the stimuli passively. Often though we really want to study the brain of an animal while it's actively performing a task or doing some natural behavior.

## 04 · 00:01:16.320 - 00:01:29.280

So we use a lot of different model organisms in neuroscience. We use mice, rats, flies, monkeys, fish, humans, among others. And that means there's a lot of different types of behaviors to study.

## 05 · 00:01:30.320 - 00:01:57.840

Reading out swimming from fish is very different from reading out flying from flies and so on. We also care about different levels of granularity depending on the questions we're asking. So sometimes we just need to know what decision a monkey is making and sometimes we want to know about the tiny little nose twitches it's making. And so all this means that there are a lot of different behavioral readouts in neuroscience and I'm not going to be able to comprehensively cover

## 06 · 00:01:57.840 - 00:02:21.840

all of them in this video. Instead I'm going to give try and give you a flavor of different types of behavioral readouts and I'll go through some example behavioral readout of decision making, complex movements, learning and memory, and internal state. I'll mostly focus on mice but a lot of the ideas contained in what I'm discussing extend to other species as well.

## 07 · 00:02:23.520 - 00:02:41.280

So if you watched the human psychophysics video from Jenny Reed, you know that a common behavioral paradigm to study decision making is the Two Alternative Forced Choice Task. And this is pretty much what it sounds like, you have two choices and you have to make a decision between them.

## 08 · 00:02:42.160 - 00:03:15.760

So I might show you a grating and ask you whether it's on the left or the right side of the screen, so here you would answer left side, and here you would answer right side. And we can vary the contrast of that grating to see what humans can perceive. The problem with animals is that they can't tell us their choice. They can't speak. So we have to have a behavioral readout of their decisions. The International Brain Laboratory just published a paper that used this exact task that

## 09 · 00:03:15.760 - 00:03:37.520

I just went through with the gratings on either side, and they had mice indicate their decisions by physically turning the wheel. So turning the wheel one way meant the grating was on the left and the other way meant it was on the right. This isn't the only way to read out positions, you can also have two spouts and mice lick at one or the other to indicate their decision.

## 10 · 00:03:37.520 - 00:03:53.520

You can have two ports and mice physically move and poke their noses into one of the two ports. With monkeys it's common to just read out their decisions based on where where they look, so they could look to the left or right, or they could use a joystick to indicate their decision.

## 11 · 00:03:55.760 - 00:04:30.640

You can also modify this task. So I'll be referring throughout this video to a study done by Simon Niesol in Ann Churchill's lab, that came out in 2019. So in this study they had mice performing a delayed 2AFC test. So while the mice were performing this task they recorded videos of them. So this is a side view of the mouse and this is a view from the bottom up. So just to orient you this is the mouse's spout, these are some spouts that can lick, these are its paws,

## 12 · 00:04:30.640 - 00:05:00.080

and these are some handles that it can grab. So in this task, in a trial, the handles come in... Oh and I'll show you a video of this in a second, but to orient you first - the handles come in, the mouse grabs the handles and that's actually what initiates the trial. But at some random time after that there's the stimuli on one side or the other. Then there's a one second delay and then the animal licks one spout or the other to indicate its decision of where the stimuli are.

## 13 · 00:05:01.120 - 00:05:30.160

And that delay is really so the act of perceiving the stimulus and the act of moving to make a decision are temporarily segregated. So I'll show you a video of one trial of this task. So the handles will come in... there... at some point the mouse will grab one of the handles which initiates the trial. In this video you can't see the stimuli but they can and then they lick one spout or the

## 14 · 00:05:30.160 - 00:05:58.640

other to indicate their decision. So just go back to that end, here you can see they're licking the spout to indicate their decision. As soon as they choose one the other spout gets out of the way. So already we have a lot of behavioral readouts of this task. So the handles actually have sensors in them so they record when the mouse grabs them. The spouts also have sensors, so they can record when the mouse licks them. We have the choice that the mouse made left or

## 15 · 00:05:58.640 - 00:06:33.200

right and we have whether it was a success or not, whether the mouse was correct and got a reward. There's a lot more going on in this video though the yellow knows pretty course rate readouts of the decisions and task related movements. So if we watch it again, it's moving its face, so some whisker movements, it's moving its hands quite a bit in a second here, um there and there's just a lot of movement that's not captured by what I just discussed. So increasingly

## 16 · 00:06:33.200 - 00:07:09.040

in neuroscience we're realizing that these more complex fine-grained movements are important to study and capture and read out, to better understand the brain. And we're increasingly focused on these complex movements and also more naturalistic behavior. And correspondingly there's been an increased focus on analysis tools and pipelines to read out behavior from these really complex behavioral videos, because these behavioral videos are amazing but they're very complex, there are a lot of pixels, so just a lot of dimensions and it's hard to do much

## 17 · 00:07:09.040 - 00:07:30.320

analysis with them. So I'm going to go for a few examples of what we can do. So we can do body part tracking. So if you see here on the fingers of the mouse's hand there are markers and if you watch as I play this video, those markers track where those fingers are at every time point.

## 18 · 00:07:31.200 - 00:08:03.360

So now instead of having just this really complex video we actually have each body part over time - the positions of it - and that's easier to work with. So you can do this manually, you can on each frame put a marker at where each body part is but that takes a while so... there has been um a software package released by neuroscientists called DeepLabCut and this will automate the process. So if you provide a few examples of where the body parts are, it trains a deep network which

## 19 · 00:08:03.360 - 00:08:26.720

is something you'll learn about in a CompNeuro course to be able to do this to all of the frames automatically, which saves you a lot of time. And this doesn't just work on mice here you can see an example of a fly you can see that we're tracking all of the body parts of the fly over time and you can see even with that complex behavior we at least can see that when the um behind

## 20 · 00:08:27.440 - 00:08:55.360

leg is moving. In the study I referred to by Simon Yisolf I didn't use deep lab cut exactly but they used similar ideas to extract information from these behavioral videos. So they actually had yet another sensor that recorded when the mouse's hind limbs moved. They extracted the pupil diameter on from this video and they also extracted when the mouse whisked, so when it moved its whiskers.

## 21 · 00:08:56.640 - 00:09:13.040

Even all that though is still very um very specific body parts and behaviors that we're capturing and there's a lot of really tiny movements like little tiny nose twitches or movements on its throat that are hard to check even with something like DeepLabCut.

## 22 · 00:09:13.760 - 00:09:46.240

So in this study they used an increasingly common technique which is to get a lower dimensional representation of this video. And I won't go through the technical details of this because you'll be learning about low dimensional representations in the CompNeuro course, but essentially at each time point instead of all of the pixels which is thousands, you can learn a lower dimensional representation so in this study they used 200 numbers. So 200 numbers at each time point conveyed most of the information and details in the video.

## 23 · 00:09:47.440 - 00:10:17.120

And that's a lot easier to work with in terms of relating to neural activity or other analyses later on. So then in this study they were also recording from the brain while the mice was the mouse was doing this task. So they used something called Wide Field Imaging and you'll actually hear from Ann Churchlind in a different video about Wide Field Imaging and see a tour of her lab. So I'm not going to go into details on that, but they record activity from

## 24 · 00:10:17.120 - 00:10:51.360

the brain and they relate it to all of these behavioral readouts I've been talking about and they find that the cortex-wide activity is really dominated by movement. Especially the uninstructed movements which are all the movements not related to the task and this is this shows us how important capturing all these behavioral readouts are because they're very important to understanding the brain because they're really influencing neural activity in the brain. I've mostly been talking about mice behaving in a head fixed way so they are in

## 25 · 00:10:51.360 - 00:11:27.120

place and can't really physically move about. But you can also look at more natural behaviors like mice roaming around. So Bob Datta at Harvard developed a method where he has mice in an open field arena and they're just being mice, doing natural behaviors and not performing a task and then he can record from above using a depth camera. This is sort of like a video camera but it actually captures the depth to the next thing below the camera. So this is really nice because

## 26 · 00:11:27.120 - 00:11:31.920

it's easier to see, for example if the mouse rears up because the depth will change at the mouse.

## 27 · 00:11:33.840 - 00:11:56.240

And then he actually developed an analysis pipeline for videos where you can extract little behavioral syllables. So we got this lower dimensional representation that i just mentioned. And then he used something called a Hidden Markov model, which again you'll learn about in the course, to extract little chunks of time where the mouse was doing something specific.

## 28 · 00:11:56.240 - 00:12:11.280

So he could automatically tell chunks of time where the mouse was walking where it was pausing and not moving much, where it was rearing. And so this allows us to really understand little component behavioral syllables that make up a mouse's behavior.

## 29 · 00:12:13.920 - 00:12:42.080

You can also use mouse navigation itself as the behavioral readout. So a common behavioral paradigm in neuroscience is the Morris Water Maze Task. And in this you literally plunk the mouse into a bucket of water and it swims around and eventually it finds a hidden platform. And it can get up on that hidden platform and out of the bucket. And if you do this a lot of times always having a hidden platform in the same place,

## 30 · 00:12:42.080 - 00:13:16.320

then the mouse after learning will swim directly towards it. And so then you can perform all sorts of manipulations, so you can put the mouse somewhere else and see how it can understand space to and if it can swim directly to the hidden platform. You can look at like mouse models of diseases if those mice have problems with this task. And all sorts of things. So the key point here is that you can use the actual navigation itself as the behavioral readout of the mouse's

## 31 · 00:13:17.120 - 00:13:21.920

learning and memory specifically with regards to spatial learning and spatial navigation.

## 32 · 00:13:24.720 - 00:13:39.760

You can also use natural behaviors to tell you about the internal state of the mouse or animal. So in the wild if a mouse sees a predator bird overhead like an eagle, it will freeze.

## 33 · 00:13:39.760 - 00:14:11.360

So it will not move at all. And we can actually take advantage of this in the lab, we can use freezing as an indirect measure of the fear of the mouse. And that means we can do things like we can shock the mouse with electric shocks that scares them in an environment and then if we put them back in the environment two days later we know if they remembered that experience, because they'll freeze more because they're scared of that environment. Similarly, we

## 34 · 00:14:11.360 - 00:14:23.680

can pair an auditory tone with the electric shocks and then we can see if the mice are conditioned to associate the tone with fear eventually, because they'll freeze just when they hear the tone.

## 35 · 00:14:26.560 - 00:15:01.280

One last behavioral readout I want to mention is using eye tracking to report where an animal is looking in the visual field so you can tell... you can use eye tracking to tell exactly where a monkey is looking at an image. And that tells you what they're paying attention to in the image or how they're parsing the image. And so as an example of what's that what that has been used for is that several studies showed images of other monkeys to their behaving monkey. And so this

## 36 · 00:15:01.280 - 00:15:26.160

is an image they showed and the blue is where the monkey looked, recorded using eye tracking. And they saw that in general the monkeys really especially looked at the eyes and they focused on the eyes and so that's actually how humans parse images too we tend to pay attention to the eyes and so we see that monkeys parse faces similarly to humans at least in that one respect.

## 37 · 00:15:27.600 - 00:15:49.120

So hopefully this video has given you an idea of the vast array of behavioral readouts we can use in neuroscience and why we might use them. In future videos you will learn about different ways of recording from the brain so that eventually we can get these behavioral readouts, we can get the neural activity, and we can start to understand what's happening.

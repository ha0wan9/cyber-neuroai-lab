# W0D0 Live in Lab - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial4.html
- YouTube: https://youtube.com/watch?v=HCx-sOp9R7M
- Caption track: en (manual)

## 01 · 00:00:00.640 - 00:00:20.800

Hi everybody, I'm Anne Churchland and this is my laboratory at UCLA in Los Angeles, California. My lab studies the neural circuits that support decision making and today I'm going to show you around my lab so you can see what people are doing and we'll dig deep into one setting called wide-field imaging that we use to measure activity across the dorsal cortex as animals are making decisions. Come with me!

## 02 · 00:00:22.800 - 00:00:45.040

We'll start up over here where two students in the lab Chaoqun and Alex are doing an experiment to understand the neural responses that support decision making. So, when the animals are doing the task as you can see let's look at these processes the same time we are using the Neuropixel system to do the ephys neural activity recording and you can see here on this monitor there are some neural spikes that we got from that.

## 03 · 00:00:46.080 - 00:01:03.600

And while we're doing the ephys recordings we're also recording the animal from above so that we can use software like DeepLabCut to track their movements. And remember ephys is one method of recording neural activity but another method, wide-field imaging, we'll be talking about shortly.

## 04 · 00:01:05.760 - 00:01:19.120

Thanks guys! Yep. And over here is Lucas. He's finding a way to measure animal behavior and it's going to show you the kind of booth that we use so that we can have animals in a situation where they're comfortable and can make good decisions.

## 05 · 00:01:21.920 - 00:01:48.400

So, we're exposing the animals to our behavioral tests in a in a sound isolated booth with minimal lighting conditions and here we can also video track the animals from the bottom or the top if we want. And we can present different stimuli and you can see here also like this is the computer which is the core like computer rig which is the core element to control behavioral stimuli and behavior and you'll see more of this later...

## 06 · 00:01:51.120 - 00:02:09.040

Thanks, Lucas. Over here we have another postdoc in the lab, Mike, who's also studying decision making he has here a behavioral rig that's the same one that you'll see in a moment in the wide-field imaging rig, but because it's out of the behavioral booth you can get a really good up close view of what it looks like and Mike can tell you a little bit more about it.

## 07 · 00:02:10.560 - 00:02:24.160

Yeah, so as you can see here this is our head-fixed setup, which has a number of sensors which also allows us to deliver auditory and visual stimuli and we can put this directly in the wide-field setup so that we can image neural activity while the animal is performing a task.

## 08 · 00:02:27.280 - 00:02:39.920

Great, Mike. Thanks for telling us about your rig. Okay now it's time to head over to the wide-field rig so you can see how all these pieces fit together and we can measure neural activity in the wide-field as animals are engaged in behavior, come on!

## 09 · 00:02:47.120 - 00:02:58.560

Hi, Ashley. Hello! This is Ashley she's an SRA in the lab and she's an expert in mouse behavior. She's going to show you what this rig looks like, the same one you saw a moment ago. Now, you'll get to see what it looks like in action!

## 10 · 00:03:01.360 - 00:03:26.080

Hello, so this is where I put my animals every single day and I train them every single day. So, just like Mike said we have two spouts with two audio-visual stimuli coming from the left side and the right side so the mice have to make their decision by either licking on the left or the right. And we also have this circuit board that we made to interact with the behavior, so we have like full control of the behavior

## 11 · 00:03:26.080 - 00:03:47.520

and this is connected to the computer as you can see right here we have the paradigm of the behavior working as well as a movie recording and this behavior is linked to another computer that is connected to the wide-field imaging so allows us to record activity with the wide-field during behavior and here is Joao to talk about the wide-field setup.

## 12 · 00:03:48.400 - 00:04:13.840

Hi Anne! This is Joao Couto, he's a postdoc in the lab and he's going to tell you about wide-field imaging. This is a setup that was originally developed by Simon Musall, when he was a postdoc in the lab and he's a co-author on the paper that Joao will tell you about where we describe this method in detail. Joao, do you want to tell the people at Neuromatch about how the light path works for wide-field imaging? Sure, Anne! Let's look at it.

## 13 · 00:04:16.080 - 00:04:44.720

So the setup actually consists of two different modules. There's an excitation module where we have a blue LED that sends light straight into the mouse brain and a violet LED also on the same module that sends light so you can correct for hemodynamics and then when light reaches the cortex it excites GCaMP, that sends green light back.

## 14 · 00:04:44.720 - 00:04:49.840

So, we have a filter where the light passes through and it goes straight into a camera

## 15 · 00:04:52.000 - 00:05:26.560

that we can use to then acquire data. We use some tricks to synchronize data and to make the lights alternate on and off between the two different wavelengths. Now, once we collect data we this would be an example of how this data look like where you can see the the whole dorsal cortex of the mouse. We can then use skull landmarks to align a reference frame like the the Allen atlas and identify different brain areas. This would

## 16 · 00:05:26.560 - 00:05:39.600

be an example over here on the on the right, of a mouse performing a decision making task and we can see that there's activation on on left trials in the right part of the brain.

## 17 · 00:05:42.720 - 00:05:58.480

We also developed this framework for sort of analyzing all these data using a cloud-based platform called NeuroCAAS, Anne do you want to tell us more about it? Fortunately, our colleagues at Columbia developed a workflow called NeuroCAAS that allows you

## 18 · 00:06:00.080 - 00:06:22.960

to do cloud-based computing even on really large data sets of the sort that you get with wide-field imaging. So, we do some of our analysis there and I'd encourage you to do the same, because it's publicly available. But one last thing: So Joao, if people are interested in building a wide-field imaging setup are they kind of just left to their own devices are there any resources they could use to help speed things along? Oooh, I forgot about that! So, we actually have a protocol

## 19 · 00:06:22.960 - 00:06:39.600

where we explain how to build a microscope but also how to do hemodynamic correction and make a skull preparation so that one can image from the entire dorsal skull of the mouse. We also discussed some steps that we can do to analyze data on the cloud.

## 20 · 00:06:40.480 - 00:07:00.240

Great! Well thanks a lot Joao. It was really great to hear about your wide-field imaging setup and how the light path works allowing you to collect neural signals from the brain. We're really enthusiastic about wide-field imaging, because it's pretty high throughput and it allows us to sample the whole dorsal cortex of the mouse which means we can look at neural activity really broadly. So, I hope you found this interesting and if you would like to analyze some wide-field data

## 21 · 00:07:00.240 - 00:07:12.960

we make lots of our data freely available online and there's more data out there also and you might discover something in the data that we didn't even know was there! So, good luck Neuromatch Academy have a great time and I hope you learned a lot in this video about wide-field imaging.

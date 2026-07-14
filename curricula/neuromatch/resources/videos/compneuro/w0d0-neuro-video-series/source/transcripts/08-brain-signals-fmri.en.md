# W0D0 Brain Signals: fMRI - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial8.html
- YouTube: https://youtube.com/watch?v=8hhQGHYsXOY
- Caption track: en (manual)

## 01 · 00:00:00.160 - 00:00:18.000

Hello, I'm Perdro Valdez-Sosa from the Cuba-China joint laboratory at the University of Electronic Science and Technology in the Cuban Neuroscience Center and I will give today a short introduction to fMRI

## 02 · 00:00:20.560 - 00:00:59.680

this is a relatively new neuroimaging technique. In fact, in 1990, Ogawa first observed so-called blood-oxygen-level-dependent effect, BOLD effect, which makes blood vessels more visible as blood oxygenation decreases, and then, here he then - and you can see the cover from the paper in science, published the first functional images using the BOLD signal from human beings, and in this case he's showing the visual cortex, which is being activated by a visual stimuli.

## 03 · 00:01:01.280 - 00:01:16.000

Now, there are many other types of fMRI techniques but we'll refer only to the BOLD signal because it's the most prevalent one. And, I have to say that since this first publication in humans

## 04 · 00:01:18.000 - 00:01:36.000

months later there were several other images of this sort each with small technical changes, and from there, there was an explosion of methods and experiments related to this technology.

## 05 · 00:01:36.000 - 00:02:14.480

Now, why has fMRI been so - let's say popular? Because it allows us, in vivo, that is to say, in live human beings study of the brain dynamics at a mesoscopic level - that is to say not at the layer of neurons nor just at the whole brain, but at intermediate levels. In fact, one speaks of spatial and temporal resolution, which tells us - it's a mathematical measure of how close can two,

## 06 · 00:02:16.000 - 00:02:27.680

let's say, points of activity, be in the brain and be distinguished, and how close in time they can be. The higher the spatial resolution, the closer and with more detail you can see it.

## 07 · 00:02:27.680 - 00:03:03.680

Likewise for time resolution. Here, we have a famous diagram which shows us in a logarithmic scale the spatial and temporal resolution, as well as the invasiveness of the different methods and we see that fMRI occupies a unique position; it's not as fast as MEG or EEG, but it certainly has more spatial resolution and can reach down to distinguish activity at the layer of columns

## 08 · 00:03:03.680 - 00:03:13.040

of layers. So, we will give an explanation of this technology saying how we measure fMRI.

## 09 · 00:03:14.000 - 00:03:35.760

What does fMRI measure? Which types of experiments can be done with fMRI? And finally, I will give some references for further reading. Now, we have to say first that fMRI is measured in an MRI machine.

## 10 · 00:03:35.760 - 00:04:10.800

You can remember that this is essentially a huge magnet with other devices like gradients, and devices for relaying radio frequency pulses. Here we see from the Cuban Neuroscience Center a 3-Tesla system, and this is how we measure the strength of the magnet - by Teslas, and on the left you actually see the magnet in all the devices where you can put the patient, And then, on the right, you see the type of imaging. Essentially, the magnet is about 60,000

## 11 · 00:04:10.800 - 00:04:35.400

times or more stronger than the magnetic field of the earth. This aligns, as you remember, the hydrogen nuclei, who are spinning like tops. They're displaced with gradients, and when they return, they emit radio frequency, and all this can be analyzed to produce spatially localized activity.

## 12 · 00:04:35.400 - 00:05:13.360

Now, there's essentially two types here that I want to distinguish of MRI: one which is structural MRI, or simply MRI, which produces very good images of structure, and on the other hand, we have functional MRI, which as I've said, is basically based on blood oxygenation. There are other techniques, and these are just two particular types of MRI images. Due to the complexity and the interplay between

## 13 · 00:05:13.360 - 00:05:51.720

the magnet, the gradients, and radio frequency, one can change the arrangement of emitting the gradients and then receiving the radio frequency response of the protons as they return to their original position. And these are known as MRI sequences, and there are many different types, and they're being still discovered at this moment, or crafted at this moment. So once again, structural MRI takes usually one image, 2D or 3D,

## 14 · 00:05:51.720 - 00:06:22.080

4 to 6 minutes. It is VERY high resolution. We have here one millimeter, there's now with higher fields, even higher resolution, and the sequences have been optimized to produce differential contrast between tissues like white matter, gray matter, and so forth. Functional MRI, on the other hand, is a dynamic series of images over time. Each image takes less than 3 seconds.

## 15 · 00:06:22.960 - 00:07:00.320

Each image can be up to 100 milliseconds in some special cases. It has lower resolution, and the sequences are optimized to be able to detect the level of oxygenation of blood or some other characteristic which is functional. And then, these sequence of images is assembled into a statistical image and we'll see about that in a minute. So, here, we see a typical experiment on the right: you see the subject, we can use a projector to put on a screen something that the subject views,

## 16 · 00:07:00.880 - 00:07:09.760

or, we can have him hearing different sounds. And in fact, he can be responding, as you can see there. Now,

## 17 · 00:07:11.680 - 00:07:33.920

we have here a typical experiment where we tell the individual to open his eyes, close his eyes, and so forth during a certain time and record several images, and then we compare these, and what you see on the top left is the stimulation of the visual cortex and visual-related areas.

## 18 · 00:07:34.800 - 00:07:38.160

And this is also an experiment that was carried out at the Cuban Center.

## 19 · 00:07:39.680 - 00:07:54.800

Now, let's go a bit into what actually is measured in fMRI. fMRI we have to be clear - and the one we're referring to is the blood oxygenation signal dependent (BOLD).

## 20 · 00:07:56.000 - 00:08:31.360

We have to remember that neurons do not have internal reserves of energy, sugar, or oxygen - neural activity needs more energy that's brought in quickly. And, it's brought in so quickly that the blood then has practically more oxygen that is really necessary, and this is known as the hemodynamic response. Now, let's take a closer look at this. Here, we have let's say in a state where there's no activation as we were seeing in the experiment we said before,

## 21 · 00:08:32.000 - 00:09:15.280

and what we're seeing there is a blood vessel, capillary, and then we see an astrocyte - one of the glial cells nearby. And here, what's happening is we see the red blood cells, erythrocytes. In red are those that are oxygenated. In blue or purple we have those which have released their oxygen to the tissue. Now, the point is that when hemoglobin has released oxygen, it's called deoxyhemoglobin, and it produces distortions of the magnetic field that

## 22 · 00:09:16.080 - 00:09:56.080

then - that's what we see on the right, let's say the magnetic field would be straight lines in the case that there's no distortion. When we have cells with deoxyhemoglobin, there's these distortions which decrease the intensity of the recorded MRI signal. On the other hand, when there's activation - that is to say, the sequence of events that we'll explain a little bit later, there's signals, there's activity going on, and there's a rush of blood cells that have oxygen there and

## 23 · 00:09:56.080 - 00:10:07.277

oxyhemoglobin does not distort the electrical fields. Therefore, we have an increase of the MRI signal.

## 24 · 00:10:07.277 - 00:10:42.160

So, to take this step by step: we have synaptic activity, so spikes arrive, the neurotransmitters are released, we see there are neuronal responses, that there's a response in time - that's occurred in time, that makes, through the astrocytes, there's a feed forward signal that produces an increase in blood flow dilation of the arterioles.

## 25 · 00:10:43.040 - 00:11:24.720

There's an increase in blood volume, there is then a decrease in deoxyhemoglobin content. This interplay between these factors and the delivery of oxygen produces what is known as the blood-oxygen-level-dependent response, and that is the response that, when we compare the inactivated state, that is before these things occur, and the activated state, allow us to identify where there's neural activity increased. And here we see the sequence, the neural response, then we have the sequence of blood volume, blood flow, and the decrease of deoxyhemoglobin,

## 26 · 00:11:24.720 - 00:12:02.360

and that is what produces the response. Now, if we look at the MRI signal over time, we see that it peaks a few seconds after there is neural activation. And people describe an initial dip where there is an initial decrease of the signal. Then, there's a post dip, but this response - hemodynamic response, is the response that's at the basis of fMRI.

## 27 · 00:12:02.360 - 00:12:29.520

Okay, which types of experiments can be carried out? And this will depend on how - using this basic technique, this will depend on how we present the stimuli and record and do the statistical analysis. So basically, I'll be talking about three different types of experiments: the block designs: you have one condition, say eyes open, another condition, say eyes closed, and then

## 28 · 00:12:31.200 - 00:13:15.200

what you do is a statistical comparison of the of the blood-oxygen-level-dependent effects of the images that are collected, and you compare these statistically, and you obtain where there's been a significant change in activity, which is then related to the difference between the two conditions, in this case, opening the eyes. And we see there an image that I showed you before. So, block designs serve to compare different conditions. On the other hand, we have what are known as event related designs, and what you do here is that you compare

## 29 · 00:13:15.840 - 00:13:50.880

different stimuli. Now, this is a very complex experiment also provided to us by Mitchell Valdes Sosa, the director of the Cuban Neuroscience Center for one of the experiments, and essentially what you have to see is that he changes what are known as Navon figures. These are figures that are bigger shapes that are composed of smaller shapes, and these shapes can be letters, and these shapes can be just blocks. And the point is that by presenting these stimuli

## 30 · 00:13:51.520 - 00:14:31.200

you can ask people to give attention either to the to the shape, let's say it's an E or a U or it's nothing, or you can also pay attention to the little symbols whether there's an E, let's say, in one of the little boxes or if it's a total E. These are very abstract types of attention processing, but then you can see that Mitchell teased out the effects related to one and the other, precisely, by using these types of different stimuli. So,

## 31 · 00:14:31.200 - 00:14:45.760

here the essence is that you have different stimuli, and then you take the activity around each stimuli, essentially, and then compare them statistically according to their conditions.

## 32 · 00:14:45.760 - 00:15:25.417

So this is more fine-grained now than the block design and it serves a different purpose. Finally, there's another type of fMRI experiment which is simply letting the person rest in the scanner, and then what you do is that you measure the activity of the brain at rest. People say it's mind wandering, people are doing just internal mental - there's no external stimuli. And the interesting thing is that Bharat Biswal

## 33 · 00:15:25.417 - 00:16:04.520

discovered in 1994, that if you take the correlation of activity between different brain regions, these brain regions are associated - that is to say, they share common activity in wide-spread networks across the brain, which have been related to different conditions and to different experiments. Now, this resting state activity and the study of so-called functional connectivity has also become a very large area of work.

## 34 · 00:16:04.520 - 00:16:26.640

So here we have the three basic paradigms. And for further reading, here are some references, some interesting textbooks, and you can see, about modeling - the last one, which is work from our own group. So thank you for your attention.

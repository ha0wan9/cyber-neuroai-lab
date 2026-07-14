# W0D0 Stimulus Representation - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial10.html
- YouTube: https://youtube.com/watch?v=-BUM4JcT9WA
- Caption track: en (manual)

## 01 · 00:00:00.320 - 00:00:29.760

Welcome to this lecture about sensory information representation. My name is Jens Kremko and my lab is located at Charite in Berlin. A central task of the brain is to integrate the outside information from the environment and to act upon it in an appropriate manner. And to do so we have many senses, with the sense of vision, smell, taste, touch, pain etc. And in today's lecture, I will briefly explain you to key concepts about how this information from the sensory environment is represented at the

## 02 · 00:00:29.760 - 00:00:34.240

level of the brain. And to introduce you to these key concepts, I will focus on the visual system.

## 03 · 00:00:38.320 - 00:01:09.280

The visual system takes up a lot of of a large part of the brain. It starts in the in the eye where the the light is detected by photo receptors and in the retina where so-called retinal ganglion cells feed this information to the visual thalamus, the LGN. The LGN is called lateral geniculate nucleus from the thalamus. From the LGN, this information is then fed forward to the primary visual cortex also called V1 which is at the back of your head.

## 04 · 00:01:10.240 - 00:01:43.760

And within V1 there's already a lot of computation taking place. And we will look at it in this lecture a little bit. But importantly from visual cortex this information is broadcasted and transmitted along many different pathways. For example, the dorsal pathway and the ventral pathway to so-called higher visual cortical areas that are important for complicated visual processing. In today's lecture, also to introduce you to the key concepts, I will mainly focus on the so-called early visual system the retina, the LGN and the V1.

## 05 · 00:01:45.360 - 00:01:50.400

So now, how do we find out how these neurons in these pathways represent sensory information?

## 06 · 00:01:52.800 - 00:02:24.240

There we can follow a systems approach. Basically we can treat the brain as a black box. And that we want to study and a very common way of approaching this question is to provide a set of inputs and then measuring the set of outputs that these inputs produce and by doing that in a systematic manner, we can slowly but steadily understand what the system is implementing and what the mechanisms are. The visual system, the input, is straightforward,

## 07 · 00:02:24.240 - 00:02:42.080

is the visual stimulus. The visual stimulus which we can represent or show on a regular computer screen. And the output is then the neural activity that we measure at the different places in the in the early digital system, for example the V1 or the LGN or the retina.

## 08 · 00:02:43.520 - 00:03:07.280

And systematically testing different stimuli, for example, this bar or upon a different orientation, we can infer, what the neurons the mechanisms of how these neurons represent the sensing information. And in the next few slides, I will give you a brief introduction to two - three key concepts that we have discovered over the last decades.

## 09 · 00:03:09.360 - 00:03:30.640

A very important concept in sensory systems is the term receptive field. A receptive field is basically the area in the sensory environment that the neuron is selected for. For example, imagine you record a neuron appearing in V1 then this neuron does not just respond to all places in the visual field. No!

## 10 · 00:03:30.640 - 00:03:42.160

It only responds to a small localized area in the visual field. And this is called receptor field. This is here shown for vision, but the same applies to for example some of the sensory system.

## 11 · 00:03:43.680 - 00:04:13.200

So that is a very important concept. Another key important concept is that the visual world is mapped in a topographic manner onto the visual cortex. What does that mean is that, a neuron that is next to it in V1, so for example, the green one in here relative to the yellow one also has a receptive field. That is not far from the receptive field of the other neuron. So the neighborhood relationship is maintained. To illustrate that further, the blue neuron here

## 12 · 00:04:13.200 - 00:04:17.040

on the right will have yet a different receptor field in a different location.

## 13 · 00:04:20.240 - 00:04:30.080

The visual field is mapped in a topographic manner onto the visual cortex and this is called a retinotopic map. And again this you also find that for example in the somatic sensory system.

## 14 · 00:04:32.320 - 00:05:03.760

How did we now find out about the receptor fields? How can we measure this? What are the techniques? How did we come up about it? And here we employed or we can use a relatively straightforward analysis method which is called Spike Triggered Averaging. As the name already implied, it simply is taking the visual stimulus, for example in our case, the visual stimulus, these for example random checkered patterns and average those in relation to the spike time. So for example,

## 15 · 00:05:03.760 - 00:05:24.320

this is the spike times our output and if we want to know what drives these neuron to spike, we simply average the stimuli that preceded the spike. And for one spike we don't see much, but if we do that across multiple spikes we can see, on average what this neuron is selected for.

## 16 · 00:05:25.360 - 00:05:41.760

This is shown here on the right, where basically here we have a number of different spikes and then over time on average we can see its receptive field. This is the visual stimulus and on average this neuron, in this example in here, responds to that localized part in the visual field.

## 17 · 00:05:44.640 - 00:06:13.520

This approach is very common in visual neuroscience and just to illustrate this a bit further, I made a little animation for you. So what you see here or what you will see here is a spike to an average example that is done on real data and on vivid data. And on the left you see the current frame that was happening around the time of the spike, and on the right you see this by to get average and here the number of spikes that were included. And it starts with just

## 18 · 00:06:13.520 - 00:06:39.680

one spike. You see that we just basically copied this frame onto the average and we don't see much. But you will see, once I start the animation and this average includes more and more spikes, you see the structure. Let me just start this, you see here, so this is the number of spikes and slowly but slowly, but steadly you see that the average emerges and the receptive field becomes evident.

## 19 · 00:06:41.360 - 00:06:52.400

And this is because very likely this neuron, when there was stimulus in this location, it spiked very often always a high probability and the noise is averaged out.

## 20 · 00:06:53.920 - 00:07:12.000

This is how we can do measure the receptive fields. And this is the receptive feed of one neuron and just to illustrate the retinotopic map, I plot here the receptive fields of three simultaneously recorded neurons and you see that the neuron one has a receptive fluid on the left, neuron two in the center and neuron three on the right.

## 21 · 00:07:13.680 - 00:07:30.800

This is just to illustrate the concept of retinotopic map. Importantly the retinotopic map is not uniform. What does it mean? It means that, our vision is not that like a camera where we just scan the visual field with with the same density of

## 22 · 00:07:32.400 - 00:08:04.320

photoreceptors or pixels, but instead our visual system has a high security. The center of its of the fixation is the fovea. This, showing you on the left where you see the visual field and this, the center fovea, where it's very tiny you know this supposed to show the first 16 degree, visual degree and it turns out that this tiny spot, here is represented at the cortical level and out of a higher magnification. This is shown here on the right side where you see the

## 23 · 00:08:04.320 - 00:08:20.880

visual cortex, kind of seen from the top and you see the retinotopic map the visual field projected onto it. And you see here on the left, on the right the fovea and you see that the first 16 degrees so this tiny spot in the visual field kind of take up almost half of the visual cortex.

## 24 · 00:08:21.680 - 00:08:38.080

I am showing this here to emphasize that the representation on the cortical level of the sense information is really tailored to the specific needs of the system. So in our case we have high spatial acuity at the center and therefore a lot of cortical network is

## 25 · 00:08:39.840 - 00:08:43.440

devoted to analyzing this the smallest part of the visual field.

## 26 · 00:08:46.240 - 00:09:14.160

In addition, so I showed you this these receptor fields in addition to just being localized these receptor fields have a lot of their dynamic and they have a lot of interesting properties. A key concept here is the so-called center and surround. The center for receptive field is really the part where visual systems drive in the neuron to spike. And the surround has a more modulatory function, so when you present stimuli in the surround you don't really drive

## 27 · 00:09:14.160 - 00:09:44.080

spiking in this in of the neuron but you can modulate. This is very nicely illustrated in the so called ON-Center and OFF-Surround cells in the retina and LGN. Likewise the OFF-Center and ON-Surround cells in the retina and LGN. So what is ON and OFF? ON and OFF are two major pathways in the visual system, so the ON pathway is there to process light increments, so everything is brighter than the average, and the OFF pathways is there to process a light decrements, the darks.

## 28 · 00:09:46.960 - 00:10:16.720

The receptive fields are shown here so the ON-Center cell responds to white spots into a small white spot, and surrounded by a dark to the OFF-Surround. And often these cells, have a so-called the center is excitatory and the surround is suppressive, shown here by the minus signs. What that means is that, if you present the light spot over the center the neuron starts to spike lot. This is shown here by the stick so this is supposed to

## 29 · 00:10:16.720 - 00:10:42.400

time these are action potentials that's the visual stimulus when you present a small spot this new one spikes quite the high firing rate. If you now extend this white disc to the suppressive of surround then this firing rate decreases. And if you even present a light annulus with a dark center then you can really suppress the firing of this ON-Center.

## 30 · 00:10:44.640 - 00:11:15.120

With the OFF-Center cell is the same thing, just inverted now a dark spot really strongly excite them and a light spot is a processor. So these ON-Center and OFF-Center of the surround sets you find in the retina and the LGN and they are kind of spot detectors. This is a cartoon, just to show you how these look at vivo, I present here on the right the receptive field measured in vivo and now color code is red ON and blue is OFF. And you can see the ON-Center cell it is a

## 31 · 00:11:15.120 - 00:11:22.080

small receptive field with a faint surround. Then OFF the center the other way around.

## 32 · 00:11:24.080 - 00:11:41.840

These are classic examples of LGN neuron receptor fields and they are often modeled as so-called difference of Gaussian where their own center is modeled as a small gauss so this excitatory part of the receptor field and the suppressor field is modeled as a cause with a wider signal.

## 33 · 00:11:42.720 - 00:11:47.600

All right, this already shows that receptive fields are dynamic and there are the interactions.

## 34 · 00:11:49.200 - 00:12:01.680

While the LGN and the retina have more these kind of spot detector receptive fields, neurons at the higher level of the visual hierarchy have often more complicated response features.

## 35 · 00:12:03.280 - 00:12:31.600

A very important response feature in this context is the so-called orientation set activity. Because it turns out that when you look in the the visual environment that it is comprised a lot about from it's contains a lot of oriented edges. For example if we take this neuromatch academy logo here, then imagine your receptive field would look here at the left, then it would kind of cover the vertical black white edge. If your receptive field would look on

## 36 · 00:12:31.600 - 00:12:55.200

the top here it would cover a horizontal edge. Yet if it would look at the 'y' over here, it would be an oblique edge. And this is an ubiquitous aspect of natural visual stimuli. And it turns out that neurons in the visual cortex are very selective to the orientation of an edge. And this is called orientation selectivity and was first discovered in cortical neurons.

## 37 · 00:12:56.560 - 00:13:25.920

It was discovered by recording neural activity in the visual cortex. And it was discovered by Hubel and Wiesel in the 50s. And they received the Nobel prize for that discovery because it's an essential aspect of visual processing and the way visual sensor information is represented at the cortical level. So what this original figure shows here is on the left the visual stimulus with horizontal and vertical bars and oblique bars, and on the right the neural activity that these

## 38 · 00:13:26.720 - 00:13:45.760

bars evoked. You see that this particular neuron preferred a vertical bar shown here with a strong responses. And then the black line here is the visual stimulus. And these responses here are or these responses are often character by so-called tuning curves.

## 39 · 00:13:46.880 - 00:14:17.760

Basically a tuning curve is a fire rate as a function of the stimulus feature that you test, for example, in this example it is the orientation of the bar and often these new enzyme contacts they have a so called this bell-shaped annotation at the tuner curve with the preferred orientation for example in this case with a vertical bar and then falling off at the flanks when the stimulus has is going away from from the preferred orientation.

## 40 · 00:14:18.800 - 00:14:37.280

Interesting about these tuning curves and you will see them a lot in sensory neuroscience is that these they are nice to characterize the selectivity, so a very narrow tuning curve represents a very selective neuron, a very broad tuning curve represents a more unselective neuron.

## 41 · 00:14:38.880 - 00:15:08.000

And this is really a key concept, the tuning curve and you find that across many different sensory systems and across different stimulus parameters. Here it is the orientation preference but you will also find tuning curves for the motion direction. So the direction of motion of the visual stimulus is a very important aspect for neurons in the visual system. I am showing you one example that is highly motion direction selective. So what you see here on the left is a color map with the

## 42 · 00:15:08.000 - 00:15:45.680

responses. On x is the time and on y the direction of motion of the moving bar and then it color codes the response strength. So when you see that this particular neuron strongly responded to a kind of downward left motion moving bar. And this then often represented in the so-called polar plot representation where the maximum firing rate for example is plotted as a function of the angle of the motion direction. You see that this particular neuron refers to the left downwards and moving

## 43 · 00:15:45.680 - 00:16:22.080

part. Yet another example of so-called spatial frequency tuning curves in of visual neurons where these are tested by so-called space by moving gratings and the grating can have a different spatial frequency. So it can be a high spatial frequency neuron grating or low spatial frequency grating and depending on the spatial frequency these neurons show this kind of tuning with a preferred spatial frequency. So these are two examples of of tunings. There are other tunings and in neurons or individual system and yet other different tunings for example

## 44 · 00:16:22.080 - 00:16:31.840

in the auditory system. But it is important these tuning curves are important concepts, for discussing how sensory information is represented at the level of the brain.

## 45 · 00:16:33.040 - 00:16:57.600

Another key aspect to this question is that, these neurons that have a certain response selectivity are not just randomly organized in visual cortex. For example when you are preferring a horizontal or vertical bar they are not just randomly intermingled in the cortical network but they they form a so-called functional map. And this I am showing here on this slide, where

## 46 · 00:16:59.200 - 00:17:17.840

this image here is a top-down view on visual cortex and the colour encodes the preferred orientation at that given location. For example, yellow region would be neurons that are responsive to vertical bars and a dark blue region neurons corresponding to horizontal bars.

## 47 · 00:17:19.040 - 00:17:55.120

And what you can see there is a beautiful so-called orientation preference map, where on the preferred orientation chain is systematically across the cortical surface. And it is, you can see these stars here, these are so called pinwheels where they it is a discontinuity where the preferred orientation changes rapidly. This has been a phenomena it has been quite studied a lot. I am showing it to represent this as a representative example for functional organization of sensory cortices. Another important aspect is that

## 48 · 00:17:56.320 - 00:18:30.720

these functional maps are often related. For example, at the same place here where we see the orientation preference map we also have a retinotopic map. And people have studied the relationship between these ways of sensory representations. The key link there, is the link of the retinotopic to the preferred orientation. This is shown here on the single cell level where I show a receptive field of it in vivo neuron measured with light spots, so the

## 49 · 00:18:30.720 - 00:18:59.360

ON response is shown in red or dark spot shown in blue here, when you overlay these ON and OFF responses so the response to lights and darks, you see that the receptive field has a almost looks like an edge like a dark light edge so this is the light part this is a dark part so it is kind of an edge detector. Remarkably the orientation of this edge and the spatial frequency matches fairly well the tuning of that neuron when measured with moving paths. This is shown here on the right

## 50 · 00:18:59.360 - 00:19:30.880

where you see the polar representation of the tuning curve, where the magenta is the prediction of the receptor field map. These so-called "simple cells" in visual cortex the kind of edge detectors and established by these ON-OFF and the light-dark receptive field aspects. They are often modeled as so-called Gabor Filters and this is also a concept that you will hear a lot about the when discussing the visual system. So these simple cell receptor fields are more or less Gabor filters which

## 51 · 00:19:30.880 - 00:19:58.240

are sine wave, sinusoidal wave multiplied with gaussian kernel. So it is a localized sine wave. The nice thing about these Gabor filters is that they have an orientation as shown here, they have a ON-OFF receptive fields, so they have spatial phase and so they are kind of localized oriented edge detectors. They are very important in the field of computation of computer vision. So

## 52 · 00:19:59.920 - 00:20:30.240

I am showing this here to illustrate there's a strong link between the retina to be and the the tuning of the moving bars on a single cell level but even on the population level there is a link just to briefly illustrate this I am showing you some slides from for my my work as a postdoc where we measured the the function organization of the visual cortex along the horizontal dimension by recording with multi-electrode arrays in vivo in the visual cortex. And we discovered that

## 53 · 00:20:33.120 - 00:20:59.760

the way the ON and OFF retinotopic so these receptor field locations are mapped onto the cortical surface that these are the origin of the orientation map. And this is shown here in this figure where you see a series of recording sites simultaneously recorded across horizontal dimension of cortex. Here you see the receptive fields that are just introduced with the ON and the OFF in red and blue near the tuning of these neurons to moving bars, and you see

## 54 · 00:20:59.760 - 00:21:35.360

that the prediction that these so-called edge detector receptive fields make in terms of the tuning preference are well matched across the entire recording length here. That means that the way the honor of retinotopic is mapped is the origin of these functional organizations. This I am just showing this here to to really stress and empathize that the the functional organization the way sense information is represented at the cortical level is very structured and highly organized and there are a lot of links between these different levels of representations.

## 55 · 00:21:37.520 - 00:22:04.880

All right, so this was about simple cells and Gabor functions oriented edges. There are many more complicated ways of how sensory information is represented. For example, i just showed the simple cells but they are also concepts called complex cells which are cells in visual cortex that are response to lights and darks irrespective of the spatial phase so whether there is the ON or OFF is left or right that doesn't matter for these cells they are

## 56 · 00:22:04.880 - 00:22:32.480

called complex, and they are also tuned and there are ideas and models of how they are generated. And even though they are called complex, they are still very simple because when we look at the visual system then as a going away from from visual cortex it's evident that the representation becomes more and more complicated. This is just shown here in this figure where this image here is first the lower level processing in the early video system decomposed in

## 57 · 00:22:33.040 - 00:22:54.720

orientation, color, contrast, disparity in motion direction etc, and then the further we go in the visual hierarchy we find the immediate level processing like shape discrimination, texture discrimination etc, then eventually at one point we go to higher level processing where we have object recognition. Finally we can recognize the code here in this image

## 58 · 00:22:56.640 - 00:23:25.120

so you see that the visual system first decomposes the visual scene into various levels of representations and then from that builds more complicated representations. What all these have in common is that, often these this level of representation are not just randomly intermixed but they are they organized in functional maps. I showed you the map for orientation and retinotopic but it turns out there are many more functional maps in visual cortex.

## 59 · 00:23:25.760 - 00:23:41.600

This is just a little cartoon here to illustrate this so here you see the orientation preference map that I just talked about but then there's another map for the eye dominance so we have two eyes, the right and the left, again that is another functioning map in visual cortex.

## 60 · 00:23:41.600 - 00:24:09.920

We can have so-called color blobs where there are regions in these maps that are that contain unions that are selective to color etc. I am really just showing this here to emphasize that this the way sensor information is represented at the level of visual cortex is highly structured; and understanding the structure and the mechanism and the origin of these structures is an important aspect of visual neuroscience and an important aspect of learning the mechanisms of how the

## 61 · 00:24:09.920 - 00:24:28.720

brain makes sense out of the outside world. With this I would like to come to the summary. In this brief lecture, I introduced you to key concepts such as receptive fields and tuning curves, just a little recap, I showed you the ON-Center OFF-Surround receptive fields

## 62 · 00:24:31.920 - 00:25:07.920

as an example of that these receptive fields are dynamic and that they are interacting and I would like to throw you to you to the video, spiking activity video as well where they also discuss this concept of center surround and receptive fields. Then I introduce you to the concept of tuning curves where we study the neural activity dependence on the stimulus feature, for example orientation preference. And I introduce you this bell shape response curves or another example the spatial frequency tuning curve. Again these concept of

## 63 · 00:25:07.920 - 00:25:34.080

tuning curves is very important for when we are discussing the sense information representation in the brain. And last I showed you one example where we can link the level of the representation for example the level of retinotopic to the level of the orientation preference tuning and this is one example there are other examples where there's a clear link between these level of representations. All right with this I am done. I would like to thank you for

## 64 · 00:25:34.080 - 00:25:41.840

your attention and if you have further questions please feel to reach out to me thank you.

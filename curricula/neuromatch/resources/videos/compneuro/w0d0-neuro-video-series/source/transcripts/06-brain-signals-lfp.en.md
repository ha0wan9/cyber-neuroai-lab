# W0D0 Brain Signals: LFP - en Subtitle Transcript

- Source page: https://compneuro.neuromatch.io/tutorials/W0D0_NeuroVideoSeries/student/W0D0_Tutorial6.html
- YouTube: https://youtube.com/watch?v=PwkYgrTE2fU
- Caption track: en (manual)

## 01 · 00:00:00.320 - 00:00:16.320

So the title of this presentation is the "Local Field Potential" often called the LFP. So what is the LFP? Well there are many ways to measure brain activity.

## 02 · 00:00:16.320 - 00:00:43.840

In particular, there are many ways to measure electrical brain activity. Neurons in, say, cortex, when they are active, sending signals like having action potentials and sending synaptic inputs to each other, they generate electrical signals that can be recorded by electrodes on the outside. And if you put electrodes on the scalp, that's called an EEG recording.

## 03 · 00:00:44.560 - 00:01:11.840

If you put it in the cortical surface, it's called an ECoG recording. Or if you have an electrode inside the population [of neurons], you can measure something called the the spikes but also what's called the local field potential. And the same bunch of active neurons also set up magnetic fields that can be measured outside the head with these MEG recordings. So

## 04 · 00:01:13.520 - 00:01:17.760

the typical analysis of these extracellular recordings inside the brain

## 05 · 00:01:19.680 - 00:01:40.720

has been to do this band-filtering into a high frequency band and a low frequency band. The high frequency band maybe about like a few hundred hertz, 500 Hz maybe, is sometimes called a multi-unit activity because this measures spikes in the individual neurons around the electrode tip.

## 06 · 00:01:43.360 - 00:02:04.640

And I would say most of the measurements and maybe the insights we have gotten from measuring from our brains in vivo has been from measuring and interpreting spikes. And the low frequency band, it's called the local field potential, has more power.

## 07 · 00:02:06.000 - 00:02:29.120

Often it has been... traditionally it was almost discarded. It wasn't even stored partially because we didn't have cheap large hard disks but also because it was more difficult to interpret because it measures sub-threshold activity due to synaptic inputs from populations of neurons.

## 08 · 00:02:29.680 - 00:02:45.280

So you cannot just look at the signal and say, "well this sort of bump comes from this particular synaptic input". You have to do a little bit more prior analysis to to interpret it in terms of

## 09 · 00:02:47.120 - 00:03:00.640

neuronal activity. However a good thing is that we know the link between the activity in neurons and these extracellularly recorded potentials.

## 10 · 00:03:02.000 - 00:03:20.080

And the link goes via the transmembrane currents of the neuron. So often when you simulate the neural activity you simulate your interest in the membrane potential in the soma because that's where it's sort of decided whether this neuron generates an action potential or not.

## 11 · 00:03:21.440 - 00:03:56.560

When you do these kind of simulations you also, as a sort of a side product, you get out all these transmembrane currents in these different parts of the neuron, different compartments. And if you know these or if you have computed these, then you can compute the potential recorded at any point, essentially any extracellular position in the brain. So for the simplest case where there's let's say, it's like an infinite homogeneous volume conductor. That's like a volume conductor

## 12 · 00:03:58.400 - 00:04:19.040

where this extracellular connectivity can be assumed to be the same everywhere and also the same in all directions, and this actually turns out to be a quite good approximation even inside the cortex even though of course outside in this extracellular space it's very convolved and so on.

## 13 · 00:04:19.600 - 00:05:02.560

To a good approximation this signal propagation inside the cortex can be modeled with a single value of this material parameter 'sigma', the extracellular conductivity. And essentially this is the formula for the simplest situation but you can also quite easily generalize this to situations where this extracellular conductivity is not constant. For example, when the signal propagates from a neuron up to the electrode and then the EEG electrode on the top of the scalp where it has to go through the skin and skull and all kinds of material with

## 14 · 00:05:02.560 - 00:05:45.840

different extracellular conductivities. So, I would say, this link between neural activity or the transmembrane currents and the extracellular potential you measure is quite well established and it applies to all signals both spikes and LFPs, EEGs and ECoG and so on. So that's good news from a modeling perspective. But the interpretation of the LFP is a bit more, as I mentioned, a bit more complicated than for spikes, which is the the extracellular signature of action potentials because a spike is much more standardized. I mean

## 15 · 00:05:50.400 - 00:06:02.240

the intracellular membrane potential signature of an action potential is quite standardized and if you keep the electrode position fixed, the extracellular shape is quite standardized also.

## 16 · 00:06:03.440 - 00:06:45.680

However with the LFP it's different because the LFP is typically generated by synaptic inputs into neurons. So then this, the recorded potential, will depend very much on where this synapse is. For example, if the synapse is positioned at an apical dendrite on this pyramidal neuron like in this case, then you get a negative excitatory current. So the current going into the neuron looks like this for an excitatory synapse.

## 17 · 00:06:45.680 - 00:06:51.600

Then close to the synapse you get this negative shape very close to the the shape of this current

## 18 · 00:06:53.120 - 00:07:24.560

and far away or close to the soma, then you get this opposite shape and this reflects a property of the cable equation which is used to model the dynamics of these neurons: that the current that goes in here must leave somewhere else. So in this case the current that goes in here from the synapse is leaving the dendrites, well quite a bit of it out, through this soma region. So that's why there the current has opposite sign, so you get this positive sign.

## 19 · 00:07:27.760 - 00:07:59.280

So there's two things to say there, one is that if you have the synapse here instead you get the opposite pattern. So for one thing you can see that it's not very local in the sense that the synaptic input here gives a large signal down here but also we see that the position of the synapse with this sort of ... when you vary the position of the synapse, the pattern can change completely. It sort of changes sign. So with many synaptic inputs you can get

## 20 · 00:08:00.000 - 00:08:21.840

all kinds of cancellation effects. So you can have a strong synaptic input, like many synapses onto the neuron, that drives it to fire rapidly but they can be placed such that the LFP that is set up is not very strong and that is illustrated here on the next

## 21 · 00:08:24.240 - 00:08:40.240

slide where we have these 10,000 biophysically detailed neural models. So this is called a stack of neurons, 10,000 of them. And this is not a very interesting network.

## 22 · 00:08:40.240 - 00:08:45.920

These neurons are not internally connected but they receive synaptic inputs from the outside. And

## 23 · 00:08:48.400 - 00:09:23.760

then you can also measure, you have this electrode that's going through the middle of this bush and this is where you can measure the local field potential. And what we see here and this on the left illustrates well where the synaptic inputs are. So first we can see now the synaptic inputs are all over the bush and you see a very small local field potential and then if it's all at the top you get a negativity there, positivity here and then when it's all at the bottom we get the opposite.

## 24 · 00:09:25.280 - 00:10:00.000

So we see that the LFP, the shape, the positivity and negativity switches place. And if it's evenly spread out you don't see anything at all. This is, on the right here, we see what you would measure at the same time with an EEG electrode, that's an electrode put on the top of the head. And so this is for the case where the population is radial meaning that ... so here illustrated is a population of neurons, this red thing here. And the signal goes through all this

## 25 · 00:10:01.600 - 00:10:15.280

cerebrospinal fluid, skull, and scalp and this is what you measure on the top. And if instead it's tangentially oriented, then you get a completely different pattern. So again

## 26 · 00:10:17.520 - 00:10:36.400

the design of the EEG and the signal, and the properties of it, very much depend on directions. And here's the same thing if you measure the magnetic field there instead. So this just illustrates that with any kind of neural model, in this case a very simple

## 27 · 00:10:38.080 - 00:10:48.480

model with 10,000 neurons, you can compute all these signals.

## 28 · 00:10:50.240 - 00:11:04.240

And for this, we have developed this tool LFPy which I think is quite useful if you want to do this kind of what you call a forward modeling of these signals based on your favorite model.

## 29 · 00:11:06.320 - 00:11:46.960

So here's another example. So, this is a network that was developed a few years ago by Potjans & Diesmann and it's a simplified model for a piece of cortex, one square millimeter, containing 80,000 neurons and they are divided into four layers. Two neuronal populations in each: one excitatory, one inhibitory. And in that case the synaptic connection rules were taken from experiments. But anyway, it's a model of a piece of cortex. However in this model

## 30 · 00:11:47.840 - 00:12:28.560

here the [neuron] models are integrate-and-fire neurons and these are point neurons so they don't have a spatial extension. And see, a point neuron, it's a single compartment. And single compartment neurons cannot generate extracellular potentials. But what you can do ... because lots of models are developed based on these point neurons and they can certainly be very efficient and good for making network models that have a good reasonable and good ... well interesting spiking dynamics.

## 31 · 00:12:30.000 - 00:13:07.040

But in order to compute also what you would measure in the local field potential, then you have to do this trick. And this is something we did a few years ago where we actually did this trick where we first compute the spiking activity in using 'nest' with point neurons and then we store all the spikes and use them in combination with multi-compartmental neurons to compute the lfp in the second step. So it's like a two-step thing. You get the

## 32 · 00:13:07.040 - 00:13:20.480

point neurons to get the spikes and then store the spikes, and then redo in some sense the simulation to compute LFP. And now also in this image/video here also the EEG.

## 33 · 00:13:23.840 - 00:13:56.480

The main point here again is to illustrate the principle but you also see in this case this visual cortex network gets an input at time 900 and we can see at that time there's this volley of activity spreading ... we're coming back to it now ... and there you go! So you see that it's like a volley of activity spreading across the cortex following this input from the thalamus and then we can see at the same time we get this activity in LFP and also in the EEG.

## 34 · 00:14:00.720 - 00:14:27.440

So what can you use this for? Well I think a key thing is that if you want to take the traditional physics approach to doing natural science, is you formulate your hypothesis in a mathematical model and then you compute, well ... take a look at what what are the consequences of this model? What kind of measurements would you do if this model was correct?

## 35 · 00:14:28.320 - 00:15:04.240

And then you compare with experiments and then you iterate back and forth until you have agreement between the model and experiments. Traditionally this has not been pursued so much at the level of networks and certainly not cortical networks. It's been difficult to make contact between a network model and specific experiments and the attempts that have been, have been in making contact with experiments in terms of the spikes that are produced.

## 36 · 00:15:06.640 - 00:15:42.400

Because that's produced by all, all models produce spikes. However a limitation, if you only compare with spikes, is that with the spikes you cannot measure spikes from many neurons at the same time. There's a limitation to how many neurons you can measure from. For example, with a little state state-of-the-art neuropixel probe if you insert those through the cortex you can maybe measure from 70–80 neurons and if you have all these different populations you end up with,

## 37 · 00:15:43.280 - 00:16:26.160

say, if you have 10 populations or well 15 populations, you end up with 5–7 neurons in each population. And these neurons are firing stochastically anyway so it's not a very a very robust signal to compare with. The LFPs on the other hand, give inherently a measure of the population activity in neurons. So this could be a better way to constrain models: in addition to comparing with spikes also compared with LFPs. So this is something we're now working on in collaboration with friends and collaborators at the Allen Institute particularly the groups

## 38 · 00:16:26.160 - 00:17:06.480

of Anton Arkhipov and Christof Koch, where we not only use their model that they produced or published in 2020 with a state-of-the-art in terms of a large-scale biologically detailed neural models. It has 250,000 neural models mimicking the mouse primary visual cortex and they also have done a lot of recordings essentially of spikes and LFPs in many-many mice

## 39 · 00:17:07.040 - 00:17:47.520

using an almost like an industrial style approach where they've done the same kind of experiments on many-many mice. So this is what we're trying to do essentially to try to make a model that can explain many of the experimental features and that is measured not only a single thing, a single feature. So what we like to call a multi-purpose model. And so that's one of the reasons we as a group are interested in computing not only spikes but also LFPs. So thank you for your attention.

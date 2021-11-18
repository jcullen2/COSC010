# Define clip audio

sourceName = getMediaPath("Desktop/Audio Python/jimmy.wav")
print sourceName
source = sourceName




def clipAudio(source, startPosition, endPosition):


  target = makeEmptySound(endPosition - startPosition)
  targetIndex = 0
  for sourceIndex in range(startPosition,endPosition):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target,targetIndex,sourceValue)
    targetIndex = targetIndex + 1

  return target




target = clipAudio(source, 0, 250000)
jimmy2 = writeSoundTo(target, '/Users/johncullen/jimmy2.wav')
audioSourceOne = makeSound(getMediaPath("/jimmy.wav"))
audioSourceTwo = makeSound(getMediaPath("/jimmy2.wav"))


def audioMixer(audioSourceOne,audioSourceTwo, splicePosition):

  length1 = getLength(audioSourceOne)
  length2 = getLength(audioSourceTwo)
  mix = makeEmptySound(length1+length2)
  mixIndex = 0
  audioSourceOneIndex = 0
  audioSourceTwoIndex = 0

  while mixIndex < length1 + length2:
    if mixIndex < splicePosition:
      audioOneValue = getSampleValueAt(audioSourceOne, audioSourceOneIndex)
      setSampleValueAt(mix,mixIndex,audioOneValue)
      audioSourceOneIndex += 1
    elif mixIndex < splicePosition + length2:
      audioTwoValue = getSampleValueAt(audioSourceTwo, audioSourceTwoIndex)
      setSampleValueAt(mix,mixIndex, audioTwoValue)
      audioSourceTwoIndex += 1
    else:
      audioOneValue = getSampleValueAt(audioSourceOne, audioSourceOneIndex)
      setSampleValueAt(mix, mixIndex, audioOneValue)
      audioSourceOneIndex += 1
  return mix

mixSound = writeSoundTo(mix, '/Users/johncullen/Desktop/mixSound.wav')

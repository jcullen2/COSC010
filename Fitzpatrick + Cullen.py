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


splicePosition = 100000
def audioMixer(audioSourceOne,audioSourceTwo, splicePosition):

  splicePosition = 100000
  length1 = getLength(audioSourceOne)
  length2 = getLength(audioSourceTwo)
  mix = makeEmptySound(length1+length2)
  mixIndex = 0
  audioSourceOneIndex = 0 
  audioSourceTwoIndex = 0 
  for mixIndex in range(splicePosition):
    
    audioOneValue = getSampleValueAt(audioSourceOne, audioSourceOneIndex)
    setSampleValueAt(mix,mixIndex,audioOneValue)
    
    audioSourceOneIndex = audioSourceOneIndex + 1
    
  for mixIndex in range(splicePosition, splicePosition + length2):
    
    audioTwoValue = getSampleValueAt(audioSourceTwo, audioSourceTwoIndex)
    setSampleValueAt(mix,mixIndex,audioTwoValue)
    
    audioSourceTwoIndex = audioSourceTwoIndex + 1
    
  for mixIndex in range(splicePosition+length2,length1+length2):
    
    audioOneValue = getSampleValueAt(audioSourceOne, audioSourceOneIndex)
    setSampleValueAt(mix,mixIndex,audioOneValue)
    
    audioSourceOneIndex = audioSourceOneIndex + 1
    
  return mix
  
mixSound = writeSoundTo(mix, '/Users/johncullen/Desktop/mixSound.wav')
  
    
  
    
    
     
   
      
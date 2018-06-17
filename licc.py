from music21 import *
import matplotlib
import scipy

licc = [0, 2, 3, 5, 2, -2, 0]

works = corpus.getComposer('bach')
for work in works:
    score = corpus.parse(work)
    for part in score.parts:
        notes = list(part.recurse().notes)
        for i, note in enumerate(notes[:len(licc)]):
            try:
                note_group = [x.pitch.midi for x in notes[i:len(licc) + i]]
                absolute = [midi - note.pitch.midi for midi in note_group]
                if absolute == licc:
                    print(notes)
                    print(i)
                    print(work)
                    print(part)
                    print(note_group)
            except:  # probably a chord
                pass

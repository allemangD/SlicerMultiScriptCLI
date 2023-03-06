import os

import SimpleITK as sitk


def gaussian(
  input: os.PathLike,
  sigma: float,
  output: os.PathLike
):
  print(f"Computing gaussian blur with {__name__}")

  reader = sitk.ImageFileReader()
  reader.SetFileName(str(input))
  image = reader.Execute()

  pixelID = image.GetPixelID()

  gaussian = sitk.SmoothingRecursiveGaussianImageFilter()
  gaussian.SetSigma(sigma)
  image = gaussian.Execute(image)

  caster = sitk.CastImageFilter()
  caster.SetOutputPixelType(pixelID)
  image = caster.Execute(image)

  writer = sitk.ImageFileWriter()
  writer.SetFileName(str(output))
  writer.Execute(image)

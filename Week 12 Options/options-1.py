class Options(dict):

  def __init__(self, *args, **kwargs):
    super().__init__()
    self.update(*args, **kwargs)

  def __getitem__(self, key):
    return self.get(key, False)

  def __getattr__(self, name):
    return self.get(name, False)

  def __setattr__(self, name, value):
    if isinstance(name, str):
      self[name] = value
    else:
      raise TypeError("Option name must be a string")

  def __delattr__(self, name):
    if name in self:
      del self[name]

  def update(self, *args, **kwargs):
    for arg in args:
      if not isinstance(arg, str):
        raise TypeError("Option name must be a string")
      self[arg] = True
    super().update(kwargs)
